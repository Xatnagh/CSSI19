// Copyright 2018 Google LLC
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//      http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
const basicAlarm = (alarmMessage) => {
    return alarmMessage;
  };
function myAlarm(myTime){
  
console.log('Hey wake up Darren, it is ' + myTime);
}
myAlarm('8:00');
function momAlarm(momTime){
    
console.log('Hey wake up mom, it is ' + momTime);
}
momAlarm('20')
function familyAlarm(familyTime,person){

console.log('Hey wake up '+person+', it is ' + familyTime);
}
familyAlarm('9','grisdel')
function importantAlarm(message){
    console.log(message.toUpperCase());
}
importantAlarm('Weeewhooos')
function snoozeAlarm(time){
    time=Number(time);
    newTime= time+1;
console.log("The alarm for " + time + "has been changed to "+newTime);
}
snoozeAlarm(10);