from django.core.exceptions import ValidationError


def get_path_upload_avatar(instance, file):
    """ The way to file, format:(media)/avatar/user_id/photo.jpg
    """
    return f'avatar/{instance.id}/{file}'

def validate_size_image(file_obj):
    """Control the size of file
    """
    megabyte_limit = 2
    if file_obj > megabyte_limit*1024*1024:
        raise ValidationError(f"File's max size not more {megabyte_limit}MB")
