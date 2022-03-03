let projectForm = document.getElementById('projectForm')
    let pageLink = document.getElementsByClassName('page-link')

    if(projectForm){
      for(let i = 0 ; i < pageLink.length ; i++){
        pageLink[i].addEventListener('click' , function(e) {
          e.preventDefault()

          let page = this.dataset.page

          projectForm.innerHTML += `<input value=${page} name = "page" hidden />`
          projectForm.submit()
        })
      }
    }

