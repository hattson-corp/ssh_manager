# ssh_manager
easy way of managing your ssh server in case of creating a a config for NapsternetV app <br>
here is the one line of installing the server manger on your linux vps :<br>
<script>var copy = function(target) {
    var textArea = document.createElement('textarea')
    textArea.setAttribute('style','width:1px;border:0;opacity:0;')
    document.body.appendChild(textArea)
    textArea.value = target.innerHTML
    textArea.select()
    document.execCommand('copy')
    document.body.removeChild(textArea)
}

var pres = document.querySelectorAll(".comment-body > pre")
pres.forEach(function(pre){
  var button = document.createElement("button")
  button.className = "btn btn-sm"
  button.innerHTML = "copy"
  pre.parentNode.insertBefore(button, pre)
  button.addEventListener('click', function(e){
    e.preventDefault()
    copy(pre.childNodes[0])
  })
})

</script>

<br>
<code > wget https://raw.githubusercontent.com/peter-hattson/ssh_manager/main/server_manager.py && mv server_manager.py /usr/bin && echo 'python3 /usr/bin/server_manger.py' > /usr/bin/server && chmod +x /usr/bin/server && echo 'now just write the command server ' </code><br>

for usage just write down the command <b><h1><code>server</code></h1></b>
<br>
keep smilling (: 
