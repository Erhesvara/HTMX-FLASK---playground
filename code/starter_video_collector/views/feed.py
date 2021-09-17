import flask
import time

from infrastructure.view_modifiers import response
from viewmodels.feed.feed_viewmodel import FeedViewModel

blueprint = flask.Blueprint('feed', __name__, template_folder='templates')


@blueprint.get('/feed')
@response(template_file='feed/index.html')
def index():
    time.sleep()
    vm = FeedViewModel()
    return vm.to_dict()
