let passOut = document.querySelector( "#pass" );
let btnGen = document.querySelector( "#gen_pass" );
// get the number input with length
function getLength(){
    return document.querySelector( "#pass_len" ).value;
}
// to allow python communication
eel.expose( setPass );
function setPass( pass ){
    passOut.value = pass;
}
document.getElementById( "gen_pass" ).onclick = () =>{
    eel.ev(getLength());
//    the input of password scale to fix with it's content
//    calculate the width
    let w = getLength() * 20;
    if( getLength() > 10 )
        w -= 20;
    else
        w += 30;
    if( getLength() > 15 )
        w += 60;
//    set the width
    passOut.style.width = w + "px";

document.getElementById("toClip").onclick = ()=>{
//    copy to clipboard
    navigator.clipboard.writeText( passOut.value );
};