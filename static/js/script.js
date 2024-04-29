let password= document.getElementById("id_password");
let confirmpass = document.getElementById("id_confirm_password");

let errorlist = document.getElementById("errorlist");



confirmpass.addEventListener("keyup",()=>{
       confrimpassword(); 
 });

function confrimpassword(){
    let password1= password.value;
    let password2=confirmpass.value;
    if (password1===password2){
        errorlist.innerText="Password is matching";
        errorlist.style.color="green";
    }
    else{
        errorlist.innerText="Password is not matching";
        errorlist.style.color="red";
    }
}





