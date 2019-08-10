
   
    $('.message').hide()
   
$(document).ready(function(){
    // setTimeout(function(){
    //     $('body').fadeIn(200)
    // },1500)

$('#create-post-heading').click(function(){
    
    $('#create-post').slideToggle(500)
})
    

// when click on edit button
$(document).on('click','#edit',function(){
    var editPost = $(this).parent()
    var title = editPost.siblings('.card-body').children('.postTitle').text()
    var post = editPost.siblings('.card-body').children('.postText').text()
    $('#post_id').val($(this).attr('data-post-id')).hide()
   
    $(" #post_title").val(title)
    $(" #post").val(post)
   
 
})



})

