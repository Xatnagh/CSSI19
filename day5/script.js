
var i;
for(i=1;i<=10;i++){
    console.log(i);
}
let result = prompt("enter your name");
console.log("hello", result);
let num = prompt("how many dankness?");
let oj = Number(num);
console.log(oj+3000);

var grade = prompt("enter your grade to determine your place in the corporate world");
var gradenum= Number(grade);
if(!isNaN(grade)&& gradenum<=70){
console.log("you passed");
}else{
    console.log("you failed");
}
