
$(document).ready(function(){
	$('#banca').DataTable();
    $('#agenda').DataTable();
    $('#confirmadas').DataTable();
    $(".dropdown-trigger").dropdown();
    $('.tooltipped').tooltip();

    $('.delete-trabalho').on('click', function(){
       deleteTrabalho(this);
       return false;
     });

     $('.email-participacao-banca').on('click', function(){
        emailParticipacaoBanca(this);
        return false;
     });

      $('#edit-form-usuario').on('submit', function(){
        url = $(this).attr('action');
        method = $(this).attr('method');
        formId = $(this).attr('id');
        editUsuario(url, method, formId);
        return false;
    });
    $('.master-menu').click(function(e){
        $(this).next('ul').slideToggle('slow');
        $('.child-menu').not($(this).next()).slideUp('slow');
    });

});

function deleteTrabalho(element){
    var url = $(element).attr('href');
    var messages = $(element).data('messages');
    var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        'url': url,
        'method': 'DELETE',
        'headers':{"X-CSRFToken": $crf_token},
        'success': function(data){
            $(element).parent().parent().remove();
            M.toast({html: messages});
        },
        'error': function(xhr, status, error){
            // console.log(xhr, xhr.responseText, status);
            loadErrors(xhr.responseJSON);
        }
    });
}

function emailParticipacaoBanca(element){
    var url = $(element).attr('href');
    var messages = $(element).data('messages');
    var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    $.ajax({
        'url': url,
        'method': 'POST',
        'headers':{"X-CSRFToken": $crf_token},
        'success': function(data){
            M.toast({html: messages});
        },
        'error': function(xhr, status, error){
            // console.log(xhr, xhr.responseText, status);
            loadErrors(xhr.responseJSON);
        }
    });
}

function editUsuario(url, method, formId){
    var formId = "#"+formId;
    var formdata = $(formId).serializeArray();
    var $crf_token = $('[name="csrfmiddlewaretoken"]').attr('value');
    var data = {};
    $(formdata).each(function(index, obj){
        data[obj.name] = obj.value;
    });


    $.ajax({
        'url': url,
        'method': method,
        'headers':{"X-CSRFToken": $crf_token},
        'data': data,
        'dataType': 'json',
        'success': function(data){
            M.toast({html: 'Seu perfil foi atualizado com sucesso'});
        },
        'error': function(xhr, status, error){
            // console.log(xhr, xhr.responseText, status);
            loadErrors(xhr.responseJSON);
        }
    });
}
