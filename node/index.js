const express = require("express");
const multer = require("multer");
const upload = multer({ dest: 'data/uploads/' });
const fs = require("fs")

var path = require('path');
const app = express();

app.use(express.static(path.join(__dirname, 'public')));


app.use(express.urlencoded( { extended: true } ));
app.use(express.json() )  

const usedIds = {"": true}
function generateNewId()
{
    let id = "";
    while(usedIds[id]) {
        id = "";
        for(let i=0; i<12; i++)
            id += Math.floor(Math.random() * 10);
    }
    return id;
}
function releaseId(id)
{
    delete usedIds[id];
}

class ProcessingRequest
{
    constructor(id, filepath, isVideo){
        this.id = id;
        this.filepath = filepath;
        this.isVideo = isVideo;
        
        // 0=Awaiting, 1=Processing, 2=Done, 3=Failed
        this.status = 0;
    }
    
    getResult()
    {
        return "<h2>RESULT: " + this.id + " FROM FILE " + this.filepath+"</h2>";
    }
}

const processingQueue = [];
const processingLookup = {};
function enqueueRequest(id, filepath)
{
    const request = new ProcessingRequest(id, filepath);
    processingQueue.push(id);
    processingLookup[id] = request;
}
function getStatus(id)
{
    return (processingLookup[id] || {status: -1}).status;
}
let isProcessing = false;
function processNextRequest()
{
    if(isProcessing || processingQueue.length <= 0)
        return;
    isProcessing = true;
    const request = processingLookup[processingQueue[0]];
    if(!request){
        processingQueue.shift();
        processNextRequest();
        return;
    }
    request.status = 1;
    delegateForAnalysis(request).then(()=>{
        processingQueue.shift();
        isProcessing = false;
        request.status = 2; // Completed
        processNextRequest();
    }).catch(err => {
        console.log(err);
        processingQueue.shift();
        isProcessing = false;
        request.status = 3; // Failed
        processNextRequest();
    });
}

function releaseRequest(id)
{
    processingLookup[id].delete();
    delete processingLookup[id];
    releaseId(id);
}

function delegateForAnalysis(request) // TODO
{
    return new Promise((resolve, reject)=>{
        setTimeout(()=>resolve(), 3000);
    });
}

app.get('/', (req, res) => {
    res.sendFile(__dirname + "/public/index.html", err => {
        if(err) {
            console.log("Error: ", err)
        }
    });
    res.end();
});

app.post('/message', (req, res) => {
    console.log(req.body);
    res.json({message: "doszło"});
})


function createDirectoryAndCopyFile(file, id)
{
    dir0 = path.join(__dirname, "data");
    dir1 = path.join(dir0, "requests");
    dir2 = path.join(dir1, id);
    
    if (!fs.existsSync(dir0)){
        fs.mkdirSync(dir0);
    }
    if (!fs.existsSync(dir1)){
        fs.mkdirSync(dir1);
    }
    if (!fs.existsSync(dir2)){
        fs.mkdirSync(dir2);
    }
    
    const filepath = path.join(dir2, file.filename + '.' + file.originalname);
    fs.renameSync(file.path, filepath);
    return filepath;
}

app.post('/upload/video', upload.any(), (req, res) => {
    if(req.files.length != 1)
    {
        res.sendStatus(400);
        res.end();
        return;
    }
    
    const file = req.files[0];
    
    console.log("ReceivedFile: ", file);
    
    const id = generateNewId();
    const filepath = createDirectoryAndCopyFile(file, id);
    
    enqueueRequest(id, filepath, true);
    processNextRequest();
    
    res.json({id: id});
    
    
})

app.post('/upload/audio', upload.any(), (req, res) => {
    if(req.files.length != 1)
    {
        res.sendStatus(400);
        res.end();
        return;
    }
    
    const file = req.files[0];
    
    console.log("ReceivedFile: ", file);
    
    const id = generateNewId();
    const filepath = createDirectoryAndCopyFile(file, id);
    
    enqueueRequest(id, filepath, false);
    processNextRequest();
    
    res.json({id: id});
    
});


app.get('/status/:id', (req, res) => {
    
    const statuses = ["Awaiting Analysis", "Processing", "Done", "Failed"];
    const id = req.params.id;
    const request = processingLookup[id];
    const status = request ? statuses[request.status] : "None";
    
    let data = {
        status: status,
        finished: request.status >= 2
    };
    
    res.json(data);
});

app.get('/result/:id', (req, res) => {
    
    const id = req.params.id;
    const request = processingLookup[id];
    
    if(!request || request.status != 2)
    {
        let result = {
            hasResult: false
        };
        
        res.json(result);
        return;
    }
    
    let result = {
        hasResult: true,
        result: request.getResult()
    };
   
    res.json(result);
})

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
    console.log("Listening on port ", PORT);
})