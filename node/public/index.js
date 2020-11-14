
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
}

function createProcessingComponent(id, type, file)
{
    const template=`
        <header>Processing ${type} file: <span class="filename">${file.name}</span></header>
        <section class="status"> 
            <section> Progress: <span id="${id}_progress_counter" >0<span>% </section>
        </section>
        <section class="result">
            <img src="" style="display:none">
        </section>
    `;
    createComponent(id, "processing", template);
}


function uploadFileForAnalisys(input, type)
{
    console.log("Sending " + type);
        
    var data = new FormData();
    data.append('file', input.files[0]);
    
    fetch("/upload/" + type,
    {
        method: "POST",
        body: data
    })
    .then(function(res){ return res.json(); })
    .then(function(data){ createProcessingComponent(data.id, type, input.files[0]) })
    .catch(function(err){ console.log(err); })
    
    console.log(type + " send");
}