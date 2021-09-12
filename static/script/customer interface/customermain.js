function helponclick(){
    document.querySelector('.main-slide').style.display="none";
    document.querySelector('.help-slide').style.display="block";
    document.querySelector('.notify').style.display="none";
}
function helponbackclick(){
    document.querySelector('.main-slide').style.display="block";
    document.querySelector('.help-slide').style.display="none";
    
}
function notifyclick(){
    document.querySelector('.main-slide').style.display="none";
    document.querySelector('.help-slide').style.display="none";
    document.querySelector('.notify').style.display="block";
}