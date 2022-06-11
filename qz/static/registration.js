var onClick=document.querySelector(".imgClick");
var eye=document.querySelector("#label-click");
var i=4;
onClick.addEventListener("click",()=>{
   
   if(i%2==0){
       eye.type="text";
       
   }else{
       eye.type="password";
   }
   i++;
})