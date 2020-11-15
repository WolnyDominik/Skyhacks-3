const express = require("express");
const multer = require("multer");
const upload = multer({ dest: 'data/uploads/' });
const fs = require("fs")

const child_process = require("child_process");

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
        if(this.status !== 2)
        {
            return undefined;
        }
        
        try{
            if(this.isVideo)
            {
                const resultPath = path.join(path.dirname(this.filepath), "film.html");
                const data = fs.readFileSync(resultPath, {encoding: "utf-8"});
                const extracted_start = data.indexOf("<body>");
                const extracted_end = data.indexOf("</body>");
                return data.slice(extracted_start+"<body>".length, extracted_end);
            }
        }
        catch(err)
        {
            console.log(err);
            return undefined;
        }
    }
}

const processingQueue = [];
const processingLookup = {};
function enqueueRequest(id, filepath, isVideo)
{
    const request = new ProcessingRequest(id, filepath, isVideo);
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
        
        setTimeout( () => {
            if(request.isVideo)
            {
                console.log("Start");
                const command = `python ../film.py ${request.filepath}`
                
                const process = child_process.exec(command, (error, stdout, stderr) => {
                
                    console.log("Lol");
                    
                    if (error) {
                        console.error(`exec error: ${error}`);
                    }
                    else
                    {
                        console.log(`stdout: ${stdout}`);
                        console.error(`stderr: ${stderr}`);
                    }
                });
                
                process.on("close", (code, signal) => {
                    console.log(`=== Closed, code: ${code}, signal: ${signal} ===`);
                    if(code === 0) {
                        resolve();
                    }
                    else {
                        reject();
                    }
                });
            }
            else
            {
                // TODO
                reject();
            }
        }, 10);
        
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
        console.log("Failed")
        res.sendStatus(400);
        res.end();
        return;
    }
    
    const file = req.files[0];
    
    console.log("ReceivedFile: ", file);
    
    const id = generateNewId();
    const filepath = createDirectoryAndCopyFile(file, id);
    
    enqueueRequest(id, filepath, true);
    res.json({id: id});
    res.end();
    
    console.log("END");
    
    setTimeout(processNextRequest, 10);
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
    res.json({id: id});
    res.end();
    
    console.log("END");
    
    setTimeout(processNextRequest, 10);
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
        result: request.getResult() || "Failed"
    };
   
    res.json(result);
})

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
    console.log("Listening on port ", PORT);
})