const API = "http://18.191.25.105:8000"

async function send(){

let msg = document.getElementById("msg").value

let res = await fetch(API+"/chat",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
message:msg,
session_id:"123"
})
})

let data = await res.json()

document.getElementById("chat").innerHTML +=
"<p><b>You:</b> "+msg+"</p>"

document.getElementById("chat").innerHTML +=
"<p><b>AI:</b> "+data.response+"</p>"
}

async function findDoctor(){

let body = document.getElementById("body").value

let res = await fetch(API+"/match_doctor?body_part="+body,{
method:"POST"
})

let data = await res.json()

document.getElementById("doctor").innerHTML =
"Doctor: "+data.doctor.name

document.getElementById("slots").innerHTML =
"Slots: "+data.available_slots.join("<br>")
}

async function book(){

let data = {
first_name: document.getElementById("first").value,
last_name: document.getElementById("last").value,
dob: document.getElementById("dob").value,
phone: document.getElementById("phone").value,
email: document.getElementById("email").value,
body_part: document.getElementById("body").value
}

let res = await fetch(API+"/book",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify(data)
})

let result = await res.json()

alert("Appointment confirmed with "+result.doctor+" at "+result.time)
}

async function voice(){

let phone = document.getElementById("phone").value

let res = await fetch(API+"/voice",{
method:"POST",
headers:{"Content-Type":"application/json"},
body:JSON.stringify({
phone:phone,
session_id:"123"
})
})

let data = await res.json()

alert(data.message)
}