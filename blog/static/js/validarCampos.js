//seleccionar el formulario a travez de la id
var formulario = document.getElementById("form1");


//asociar funcion validar al hacer click

window.onload=iniciar;//sin parentesis

//funcion iniciar 
function iniciar(){

    document.getElementById("enviar").addEventListener('click',validar,false);
}

//seleccion de elementos 

function validaNombre(){

    var nombre=document.getElementById("nombre");
    if(nombre.value == ""){
        alert("El nombre no puede estar vacio");
        return false;
    }else if(!nombre.checkValidity()){

        alert("El nombre solo puede contener letras");
    }
    return true;
}


function validarCorreo(){

var correo=document.getElementById("correo").value;
var expresion = /\w+@\w+\.+[a-z]/;
if(correo.value ==""){

    alert("El correo esta vacio");
    return false;
}else if (!expresion.test(correo)) {

    alert("Formato de correo invalido");
    return false;


}
return true;
}

function validarRut(){

var correo= document.getElementById("rut");
if (!correo.checkValidity()){

    alert("El rut es invalido");
    return false;
}
return true;
}



//funcion que valida elementos 
function validar(e){

    if(validaNombre()&&validarCorreo()&&validarRut()&&confirm("Cliquea SI para enviar formulario")){
        alert("Registro realizado");
        return true;
       
    }else{
        alert("Registro no  realizado");
        e.preventDefault();
        
        return false;
    }
}