setInterval(() => {
    const socket = new WebSocket("ws://192.168.0.103:8080");
    const jsonURL = browser.extension.getURL('adsBlocker/findedAds.json')

    socket.addEventListener("open", (event) => {
        var html = document.getElementsByTagName('html')[0].innerHTML
        socket.send(html);
        html = null;
    });

    socket.addEventListener("message", (event) => {
        
        
        if(event.data === 'True')
        {
            fetch(jsonURL)
            .then(response => response.json())
            .then(json => {
                var classAd = json.Class
                if(classAd !== null)
                {
                    for(var elementClass in classAd)
                    {
                        var elements = document.getElementsByClassName(`${classAd[elementClass]}`)
                        if(elements)
                        {
                            for(var index = 0; index < elements.length; index++)
                            {
                                elements[index].style.display = "none"
                            }
                        }
                    }
                }
                var IDad = json.ID
                if(IDad !== null)
                {
                    for(var elementID in IDad)
                    {
                        var element = document.getElementById(`${IDad[elementID]}`)
                        if(element)
                        {
                            element.style.display = "none"
                        }
                    }
                }
                var SRCad = json.SRC
                if(SRCad !== null)
                {
                    for(var elementSRC in SRCad)
                    {
                        var element = document.querySelector(`[src="${SRCad[elementSRC]}"]`)
                        if(element)
                        {
                            element.remove()
                        }
                    }
                }
                var HrefAd = json.Href
                if(HrefAd !== null)
                {
                    for(var elementHref in HrefAd)
                    {
                        var element = document.querySelector(`[href="${HrefAd[elementHref]}"]`)
                        if(element)
                        {
                            element.remove()
                        }
                    }
                }
                var DataAd = json.Data
                if(DataAd !== null)
                {
                    for(var elementData in DataAd)
                    {
                        var element = document.querySelector(`[data="${DataAd[elementData]}"]`)
                        if(element)
                        {
                            element.style.display = "none"
                        }
                    }
                }

            })
            .catch(error => console.error('Error loading JSON:', error));
        }
        else
        {
            console.log('Error from server')
        }
    });

    socket.addEventListener("close", (event) => {
        console.log("Connection closed")
    });
},3000);