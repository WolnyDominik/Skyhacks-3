
let processingIds = {};

function sendVideo(input)
{
    console.log("Sending Video");
        
    var data = new FormData();
    data.append('file', input.files[0]);
    
    fetch("/upload/video",
    {
        method: "POST",
        body: data
    })
    .then(function(res){ return res.json(); })
    .then(function(data){ processingIds[data.id] = true; })
    .catch(function(err){ console.log(err); })
    
    console.log("Video Send");
}
function sendAudio(input)
{
    console.log("Sending Audio");
    
    var data = new FormData();
    data.append('file', input.files[0]);
    
    fetch("/upload/audio",
    {
        method: "POST",
        body: data
    })
    .then(function(res){ return res.json(); })
    .then(function(data){ processingIds[data.id] = true; })
    .catch(function(err){ console.log(err); })
    
    console.log("Audio Send");
}