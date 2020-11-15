
let processingIds = {};


function setup()
{
    document.getElementById("file_upload_video").addEventListener('change', (e)=>{
        uploadFileForAnalisys(e.target, "video");
    });
    document.getElementById("file_upload_audio").addEventListener('change', (e)=>{
        uploadFileForAnalisys(e.target, "audio");
    });
    
    uploadButtons = document.getElementsByClassName("upload_button");
    for( element of uploadButtons) {
        element.addEventListener('click', e => {
            document.getElementById(e.target.getAttribute('destination_file_input')).click();
        });
    }
}

setup();

function createComponent(id, classname = "", innerHTML = "")
{
    let component = document.createElement('section');
    component.setAttribute("class", "component " + classname);
    component.setAttribute("id", id);
    component.innerHTML = innerHTML;
    document.getElementById("components_container").appendChild(component);
    const component_ = new Component(component);
    setTimeout(()=>component_.element.style.opacity = "1", 100);
    return component_;
}

class Component
{
    constructor(element)
    {
        this.element = element;
    }
    
    delete()
    {
        this.element.parentElement.removeChild(this.element);
    }
}

function createSendingComponent(file)
{
    return createComponent("", "sending", `<section>Sending file: <span>${file.name}</span>, (${file.size} bytes)`);
}

function refreshStatus(component)
{    
    console.log("refreshing");
    fetch('/status/' + component.id, 
    {
        method: "GET"
    })
    .then(function(res){ return res.json(); })
    .then(function(data){ 
        
        document.getElementById(component.id + "_progress_counter").innerHTML = data.status;
        if(data.finished)
        {
            console.log("FINISHED", component.id);
            setProcessingResult(component);
        }
        else
        {
            setTimeout(()=>refreshStatus(component), component.refreshInterval);
        }
        
     })
    .catch(function(err){ console.log(err); });
}

function setProcessingResult(component)
{
    console.log("fetching result");
    fetch('/result/' + component.id,
    {
        method: "GET"
    })
    .then(function(res){ return res.json(); })
    .then(function(data){ 
        
        if(!data.hasResult){
            document.getElementById(component.id + "_result").innerHTML = "Result: None";
            return;
        }
        document.getElementById(component.id + "_result").innerHTML = data.result;
        
        
     })
    .catch(function(err){ console.log(err); });
}

function createProcessingComponent(id, type, file)
{
    const template=`
        <header>Processing ${type} file: <span class="filename">${file.name}</span></header>
        <section class="status"> 
            <section> Progress: <span id="${id}_progress_counter" >0%<span> </section>
        </section>
        <section class="result" id="${id}_result">
        </section>
        <section class="player">
        ${type=="video"?`<video width="320" height="240" controls> <source src="${file}" type="video/mp4"> <source src="${file}" type="video/mov">`
        :` <audio controls>  <source src="${file}" type="audio/mpeg"> Your browser does not support the audio element. </audio> `}
        <section class="player">
        
    `;
    component = createComponent(id, "processing", template);
    component.id = id;
    component.filename = file.name;
    component.refreshInterval = 200;
    refreshStatus(component);
}


function uploadFileForAnalisys(input, type)
{
    console.log("Sending " + type);
    
    var data = new FormData();
    data.append('file', input.files[0]);
    
    
    let sendingComponent = createSendingComponent(input.files[0]);
    
    fetch("/upload/" + type,
    {
        method: "POST",
        body: data
    })
    .then(function(res){ return res.json(); })
    .then(function(data){ createProcessingComponent(data.id, type, input.files[0]) })
    .catch(function(err){ console.log(err); })
    .then(function(){ sendingComponent.delete(); })
    
    console.log(type + " send");
}