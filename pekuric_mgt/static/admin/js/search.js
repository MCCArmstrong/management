
function makeSearchRequest(){
    if(document.getElementById("search_keyword").value == ""){
        document.getElementById("search_keyword").innerHTML = ""
        return;
    }
    let request = new XMLHttpRequest()
    let keyword = document.getElementById("search_keyword").value
    request.open("GET", window.location.origin+"/admin/search-product/?query="+keyword, true);
    request.onreadystatechange = function(e){
        if(e.target.readyState == 4 && e.target.status == 200){
           let response = JSON.parse(e.target.response)
           for(let index in response){
                let data = response[index]
                document.getElementById("search_list").innerHTML = `
                    <li class="list-group-item">
						<div style="width:50px;">
						    <img src="" alt="Look for the file bitch!" style="width:100%">
						</div>
						${data.sliders}
						<b>${data.description}</b>
						<b>${data.preview}</b>
					</li>  `
           }
        }
    }
    request.send();
}