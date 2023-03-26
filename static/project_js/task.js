
     
		var task="default";
		var date="default";
		var check="default";
		var id=null


		function getCookie(name) {
			var cookieValue = null;
			if (document.cookie && document.cookie != '') {
				var cookies = document.cookie.split(';');
				for (var i = 0; i < cookies.length; i++) {
					var cookie = jQuery.trim(cookies[i]);
					// Does this cookie string begin with the name we want?
					if (cookie.substring(0, name.length + 1) == (name + '=')) {
						cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
						break;
					}
				}
			}
			return cookieValue;
		}

 
  
		var activeItem = null
		var list_snapshot = []

		buildList()

		function buildList(){
			var wrapper = document.getElementById('list-wrapper')
			//wrapper.innerHTML = ''



			var url = 'http://127.0.0.1:8000/task-list/'

			fetch(url,{
				method: 'POST',
				body: JSON.stringify({
		
				  id:{{user.id}},
			  
			}),
			headers: {
				'Content-type': 'application/json; charset=UTF-8',
			  }
		})
			.then((resp) => resp.json())
			.then(function(data){
				

				var list = data
				for (var i in list){


					try{
						document.getElementById(`data-row-${i}`).remove()
					}catch(err){

					}
			

                    var myobject=list[i]
					console.log(myobject,"all objects")
					var title = `<span class="title text-primary " >${list[i].task}</span>`
					var check_element=`<input class="form-check-input" type="checkbox" onchange="getCheck(this)" id="completed" >`
					var status=`<span class="badge badge-warning ml-2">pending</span>`
					if (list[i].task_completed == true){
						title = `<strike class="title text-primary " >${list[i].task}</strike>`
						check_element=`<input class="form-check-input" type="checkbox" onchange="getCheck(this)" id="completed" checked>`
						status=`<span class="badge badge-default ml-2">completed</span>`
					}
                   var date=list[i].task_date
				   var parts =date.split('-')
				   var currectdate=new Date(parts[0],parts[1],parts[2])
				   //console.log(currectdate,"my date")
					var item = `
						<div id="data-row-${i}" class="task-wrapper flex-wrapper">
							
							<div style="flex:5" class="text_div ">
								${title}
							</div>
							<div style="flex:2">
								${status}
							</div>
							<div style="flex:3">
								${list[i].task_date}
							</div>
							
							
							<div style="flex:1">
								<button class="btn btn-sm btn-outline-info " data-toggle="modal" data-target="#modal${list[i].id}">Edit </button>
							</div>
							<div style="flex:1">
								<button class="btn btn-sm  delete" data-toggle="modal" data-target="#deletemodal" onclick="setId(${list[i].id})">-</button>
							</div>
							
						</div>
						

						<div class="modal fade" id="modal${list[i].id}" tabindex="-1" role="dialog" aria-labelledby="myModalLabel"
						aria-hidden="true">
						<div class="modal-dialog" role="document">
						  <div class="modal-content">
							<div class="modal-header text-center">
							  <h4 class="modal-title w-100 font-weight-bold">Edit Task</h4>
							  <button type="button" class="close" data-dismiss="modal" aria-label="Close">
								<span aria-hidden="true">&times;</span>
							  </button>
							</div>
							<div class="modal-body mx-3">
							  <div class="md-form mb-5">
								<form  id="myform" >
								<i class="fas fa-tasks prefix grey-text"></i>
								<input type="text" id="task_edit" class="form-control validate" onchange="getTask(this.value)" value=${list[i].task}>
								
							  </div>
					  
							  <div class="md-form mb-5 child">
								<i class="fas fa-calendar prefix grey-text"></i>
								<input type="date" id="date_edit" value=${String(list[i].task_date)} onchange = "getDate(this.value)" class="form-control validate">
								
							  </div>
					  
							 
					  
							  <div class="form-check">
								${check_element}
								<label class="form-check-label" for="flexCheckDefault">
								  completed
								</label>
							  </div>
					  
							</div>
							<div class="modal-footer d-flex flex-column justify-content-center">
							  <button type="button" class="btn btn-unique edit" onclick="editItem(${myobject.id})"  >Edit</button>
							  <div class="text-warning fw-bold" id="error" ><div>
							</div>
						</form
						
						  </div>
						</div>
					  </div>

					`
					wrapper.innerHTML += item
					
	
				}
    
				if (list_snapshot.length > list.length){
					for (var i = list.length; i < list_snapshot.length; i++){
						document.getElementById(`data-row-${i}`).remove()
					}
				}

				list_snapshot = list



			})
		}
		function setId(value){
			id=value
			console.log("delete id",id)
		}

		function delete_task(){

			fetch(`http://localhost:8000/modelview/${id}/`,{
				method: 'DELETE',
				
				headers: {
				  'Content-type': 'application/json; charset=UTF-8',
				  
				}
				}).then(function(response){
					
					return response.json()
				
				}).then(function(data){
					console.log("delete data",data.msg)
					buildList()
				})
		}

		function getDate(value){

			date=value
			
			console.log(date,"hope date")
		}
		function getTask(value){
            task=value
			
			console.log(task,"hopetask")
		}
		function getCheck(checkbox){

		

			if (checkbox.checked) {
				checkbox.value="completed"
				check="completed"
				console.log(check)
			  } else {
			
				check="not completed"
					console.log(check);
			  }
		}
	
       function editItem(myobject){
	   	var task_edit;
		var date_edit;
		var check_edit;
   
   

	   console.log(task,date,check)
	   if(task=="default"){
		
		task_edit="default"
	   }
	   else{
		task_edit=task
	   }
	   if(date=="default"){
		date_edit="default"
		
	   }
	   else{
		date_edit=date
	   }

	   if(check=="default"){
		check_edit="default"
		
	   }
	   else{
		check_edit=check
	   }
		fetch(`http://localhost:8000/modelview/${myobject}/`,{
			method: 'PATCH',
			body: JSON.stringify({
		
			  task:task_edit,
			  task_date:date_edit,
			  task_completed:check_edit
		
		
		  
			}),
			headers: {
			  'Content-type': 'application/json; charset=UTF-8',
			  
			}
			}).then(function(response){
				
				return response.json()
			
			}).then(function(data){
				console.log("edit data",data.msg)
				if(data.msg !="no updations"){

					var mymodals =document.getElementsByClassName("modal")
					var backdrop=document.getElementsByClassName("modal-backdrop")
					backdrop[0].remove()
				while (mymodals.length > 0) {
                         mymodals[0].remove();
                        }
					buildList()
				
					//mymodal.style.display="none";
					//mymodal.modal('hide');
					//$(`#modal${myobject}`).modal("toggle");
					



				}
				else{
               var sel=document.getElementById("error")
			   console.log(sel)
			   sel.innerHTML="<p>make some edits</p>";
				}
			
			})

	   }


		function createtask(){
			var task=document.getElementById("title").value
			var date=document.getElementById("date").value
			var csrftoken = getCookie('csrftoken');
			console.log(date,"entered date",csrftoken)
			
			fetch('http://localhost:8000/modelview/', {
				method: 'POST',
				body: JSON.stringify({
			
				  task:task,
				  task_date:date,
				  user:{{user.id}}
			
			
			  
				}),
				headers: {
				  'Content-type': 'application/json; charset=UTF-8',
				  'X-CSRF-Token': csrftoken
				}
				})
				.then( function(response){ 
					buildList()
			
				return response.json()
				}).then(function(data){
					console.log(data)
				})
			
			  }
			  

