let password= document.getElementById("id_password");
let confirmpass = document.getElementById("id_confirm_password");
let submitbtn = document.getElementById("submitbtn");
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
        submitbtn.type="submit";
    }
    else{
        errorlist.innerText="Password is not matching";
        errorlist.style.color="red";        
        submitbtn.type="button";
       
    }
}


console.log(submitbtn);



