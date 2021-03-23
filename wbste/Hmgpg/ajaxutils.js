(function (global) {
	var ajaxUtils ={};

	function getRequestObject(){
		if (window.XMLHttpRequest){
			return (new XMLHttpRequest())
		}
		
		

	}

	ajaxUtils.sendGetRequest = function(requestUrl, responseHandler){
			var request =getRequestObject();
			
			request.onreadystatechange = function(){
					handleResponse(request,responseHandler)
				}
			request.open("GET", requestUrl, true)
			request.send(null)
		}
	function handleResponse(request, responseHandler){
		if((request.readystate == 4) && (request.status==200)){
			request(request)
		}
	}
	global.$ajaxUtils = ajaxUtils


})(window);