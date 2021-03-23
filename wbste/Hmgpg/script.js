document.addEventListener("DOMContentLoaded",
    function(event){
        document.querySelector("#btn").addEventListener("click", function(){
                
                

            $ajaxUtils.sendGetRequest("http://localhost:3000/name.txt",
                    function(request){
                         var name = request.responseText;
                         console.log(name);
                        document.querySelector("#cnt").innerHTML="<h2> hello " + name + "!</h2>";
                    })
                    
            
                }
                )}
    
)