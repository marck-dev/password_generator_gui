let passOut = document.querySelector( "#pass" );
let btnGen = document.querySelector( "#gen_pass" );
function getLength(){
    return document.querySelector( "#pass_len" ).value;
}
eel.expose( setPass );
function setPass( pass ){
    passOut.textContent = pass;
}
document.getElementById( "gen_pass" ).onclick = () =>{
    eel.ev(getLength());
};