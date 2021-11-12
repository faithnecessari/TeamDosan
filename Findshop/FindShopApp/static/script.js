<script>
  (function () {
  'use strict'
  const forms = document.querySelectorAll('.requires-validation')
  Array.from(forms)
    .forEach(function (form) {
      form.addEventListener('submit', function (event) {
      if (!form.checkValidity()) {
          event.preventDefault()
          event.stopPropagation()
      }
    
        form.classList.add('was-validated')
      }, false)
    })
  })()

  //function checkPassword(){
  //  let Password = document.getElementById("Password").value;
  //  let ConPass = document.getElementById("ConPass").value;
  //  console.log(Password,ConPass);
  //  let message = document.getElementById("message");

  //  if(Password.length != 0){
  //    if(Password == ConPass){
  //      message.textContent = "Password match!";
  //    }else{
   //     message.textContent = "Password don't Match!";
   //   }
  //  }
 // }
  </script>