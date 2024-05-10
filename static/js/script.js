let password= document.getElementById("id_password");
let confirmpass = document.getElementById("id_confirm_password");
let submitbtn = document.getElementById("submitbtn");
let errorlist = document.getElementById("errorlist");
let  emailvalue=document.getElementById("id_email");


errorlist.style.fontSize="25px";
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
        console.log(document.querySelector("input"));
    }
    else if(password2===""){
        errorlist.style.display="none";
        submitbtn.type="button"
    }
    else{
        errorlist.style.display="";
        errorlist.innerText="Password is not matching".toUpperCase();
        errorlist.style.color="white";  
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
        errorlist.style.color="white";
    }
  }



function onbutton(){
    document.getElementById("loginbtn").addEventListener("mousedown",()=>{
        document.getElementById("loginbtn").style.color="red";
    })

    document.getElementById("loginbtn").addEventListener("mouseup",()=>{
        document.getElementById("loginbtn").style.color="green";
    })
}





function onb(){
    console.log(document.querySelectorAll("input"));
}


onb()