function checkValidation()
{
    var isValid = true;
    if($("#date").val() == null){
        isValid = false;
    }
    if($("#name").val() == null){
        isValid = false;
    }
    if($("#email").val() == null){
        isValid = false;
    }
    if($("#phone").val() == null){
        isValid = false;
    }
    if($("#people").val() == null){
        isValid = false;
    }
    return isValid;
}

$(document).on('click', submit, function(e){
    e.preventDefault();
    var validated = checkValidation();
    if(validated == true){
        $('#myModal').modal('show');
    }
});
