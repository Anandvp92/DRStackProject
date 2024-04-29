let password= document.getElementById("id_password");
let confirmpass = document.getElementById("id_confirm_password");
let submitbtn = document.getElementById("submitbtn");
let errorlist = document.getElementById("errorlist");
let  emailvalue=document.getElementById("id_email");

emailvalue.addEventListener("keyup",()=>{
    emailvalidation();
})
confirmpass.addEventListener("keyup",()=>{
       confrimpassword(); 
 });

function confrimpassword(){
    let password1= password.value;
    let password2=confirmpass.value;
    if (password1===password2){
        errorlist.style.display="none";
        submitbtn.type="submit";
    }
    else if(password2===""){
        errorlist.style.display="none";
        submitbtn.type="button"
    }
    else{
        errorlist.style.display="";
        errorlist.innerText="Password is not matching".toUpperCase();
        errorlist.style.color="red";        
        submitbtn.type="button";       
    }
}


function emailvalidation() {
   let validRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

    outvalue= emailvalue.value;
    if(outvalue.match(validRegex)){
        
        errorlist.style.display="none";
    }
    else if(outvalue===""){
        errorlist.style.display="none";

    }
    else{
        errorlist.style.display="";
        errorlist.innerText="Email is not valid".toUpperCase();
        errorlist.style.color="red";
    }
  }



