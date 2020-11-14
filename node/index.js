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
    delete usedIds[id]
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
    
    fs.renameSync(file.path, path.join(dir2, file.filename + '.' + file.originalname));
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
    createDirectoryAndCopyFile(file, id);
    
    res.json({id: id});
    
    // TODO start processing
    
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
    createDirectoryAndCopyFile(file, id);
    
    res.json({id: id});
    
    // TODO start processing
    
})


app.get('/status/{id}', (req, res) => {
    
    // TODO calculate status
    
    let status = {};
    status.progress = 0.1;
    status.done = false;
    
    res.json(data);
});

app.get('/result/{id}', (req, res) => {
    
    // TODO create result
    
    let result = {}
    
    res.json(result);
})

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
    console.log("Listening on port ", PORT);
})