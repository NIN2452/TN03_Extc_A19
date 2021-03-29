 function validate()
        {
            if(document.getElementById('username').value=="Doctor")
            {   if(document.getElementById('password').value=="12345")
                {
                    window.location.replace("https://nin2452.github.io/TN03_Extc_A19/wbste/Doctor/index.html");
                }
                else
                {
                    alert("Wrong Password")
                }
            }
            else if(document.getElementById('username').value=="Receptionist")
            {   if(document.getElementById('password').value=="12345")
                {
                     window.location.replace("https://nin2452.github.io/TN03_Extc_A19/wbste/Receptionist/index.html");    
                }
                else
                {
                    alert("Naaay")
                }
            }
            else if(document.getElementById('username').value=="Pathologist")
            {   if(document.getElementById('password').value=="12345")
                {
                     window.location.replace("https://nin2452.github.io/TN03_Extc_A19/wbste/Pathologist/homepg.html");
                }
                else
                {
                    alert("Naaay")
                }
            }
            else if(document.getElementById('username').value=="Atharva")
            {   if(document.getElementById('password').value=="12345")
                {
                     window.location.replace("https://nin2452.github.io/TN03_Extc_A19/wbste/1.html");
                }
                else
                {
                    alert("Naaay")
                }
            }
	        else{alert("nay")} 

        }
    function goto()
    {
        window.location.replace("https://nin2452.github.io/TN03_Extc_A19/wbste/registration.html");
    }