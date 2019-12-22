import MediaController from './controllers/layouts/media_controller';
import PictureController from './controllers/fields/picture_controller';
import UploadController from './controllers/fields/upload_controller';

if (typeof window.application !== 'undefined') {
    window.application.register('fields--picture', PictureController);
    window.application.register('fields--upload', UploadController);
    window.application.register('layouts--media', MediaController);
}
