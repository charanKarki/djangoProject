var data
$(document).ready(function () {
    // get blog posts when document is loading
// blog post rendering function 

    $.get('/showposts/','json',function(blogData){
        // console.log(data)
        $.get('/likes/',function(likeData){

            for(let post of blogData){
                post.like=0
                for (let like of likeData){
                    if(post.id==like.post)
                        post.like++
                }
                appendData_To_BlogContainer(post)
                
            }
            console.log(blogData,likeData)
            // $(".love").append(data)
        })
        
        
    })
 
    
//  ajax request on blog create
// $("#create-post").on('submit',function(e){
//     e.preventDefault()
//     var list = []
//     var formData = new FormData($("#create-post")[0])
//     formData.forEach(function(i){
//         list.push(i)
//     })
//     $.post('/showposts/',formData.getAll(),
//     function(post){
//         appendData_To_BlogContainer(post)
//         $("#create-post")[0].reset()
        
//     },'json'
//     )
// })   

// likes on cliek event
$(document).on('click','.love',function(){
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    var btn = $(this)
    var like = 'true'
    var id = $(btn).attr('data-post-id')
    var val = Number($(btn).children('p').text())
    $(btn).children('p').text(val+1)
    $(btn).children('i').removeClass('text-white bg-dark').addClass('text-danger bg-light').css('transform','scale(1.2rem)')
    $.ajax({
        type: "post",
        url: "/likes/",
        data: {
            'id':id,
            'like':like,
            'csrfmiddlewaretoken':csrftoken
        },
        dataType: "txt",
        success: function (data,response) {
            console.log(data,response)
           
        }
    });
})


   
// request on blog delete on click
$(document).on('click','.delete',function(){
    var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
    var post = $(this)
    var card =post.parent().parent()
      // ajax request
    $.ajax({
        type: "post",
        url: "/deleteItem/",
        data:{'Id':Number(post.attr('data-post-id')),'csrfmiddlewaretoken':csrftoken},
        
        success: function (data,response) {
            
            $(card).fadeOut(200,function(){
            $('.message').show().text(`${data}`).addClass('text-light bg-danger ').hide(1000)
                // update posts
                // showPostData()
            })     
        }})
})



});

function appendData_To_BlogContainer(post){
    
        var date = new  Date(post.date)
        date= date.toDateString()
        $("#postSlide ").append(`

        <div class="card col-sm-6 col--md-4 col-lg-3">
        <img class="card-img postImg" src="${post.post_img}" title="${post.post_img}">
        <div class="card-body bg-light text-dark my-2 p-3">
            <h4 class="card-title postTitle" >${post.post_title} </h4>
            <p class="card-text postText" >${post.post}</p>
        
           
            </div>
            <div class="card-footer text-center">
            <p class="text-left card-subtitle font-weight-bold">By ${post.user}</p> <p class="text-right font-weight-bold text-dark" style="font-size: .7rem">${date}</p> 

                
                <!-- edit buttons --> 
            
                

                <button class=" love"data-post-id=${post.id}><i class="fa fa-heart btn bg-dark text-white btn-sm"  ></i> </br><p>${post.like}</p></button>                    
                <button type="submit" class="btn bg-danger text-white btn-sm  delete" data-post-id=${post.id}><i class="fa fa-trash" aria-hidden="true"></i></button>
                <button  class="btn bg-dark text-white btn-sm edit" id='edit'data-post-id=${post.id} data-toggle="modal" data-target="#modelId"><i class="fa fa-edit"></i></button>
                <button  class="btn bg-dark text-white btn-sm comment" id='edit'data-post-id=${post.id}><i class="fa fa-comment" aria-hidden="true"></i></button>
                
           
            

            </div>

        
     </div>    

        `)
    
}
