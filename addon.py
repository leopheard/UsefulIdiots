from xbmcswift2 import Plugin, xbmcgui
from resources.lib import mainaddon

plugin = Plugin()
url1 = "https://feeds.megaphone.fm/usefulidiots"
@plugin.route('/')
def main_menu():
    items = [
        {
            'label': plugin.get_string(30001), 
            'path': plugin.url_for('episodes1'),
            'thumbnail': "https://megaphone-prod.s3.amazonaws.com/podcasts/1f0793d6-b87b-11e9-8b85-a71716e1a0b1/image/uploads_2F1565295633147-ihglfm637uc-8445ebe4c08962936d198157dd258ebb_2FUseful%2BIdiots_FINAL_3000px.jpg"},
        {
            'label': plugin.get_string(30000),
            'path': plugin.url_for('episodes'),
            'thumbnail': "https://megaphone-prod.s3.amazonaws.com/podcasts/1f0793d6-b87b-11e9-8b85-a71716e1a0b1/image/uploads_2F1565295633147-ihglfm637uc-8445ebe4c08962936d198157dd258ebb_2FUseful%2BIdiots_FINAL_3000px.jpg"},
    ]
    return items

@plugin.route('/episodes1/')
def episodes1():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast1 = mainaddon.get_playable_podcast1(soup1)
    items = mainaddon.compile_playable_podcast1(playable_podcast1)
    return items

@plugin.route('/episodes/')
def episodes():
    soup1 = mainaddon.get_soup1(url1)
    playable_podcast = mainaddon.get_playable_podcast(soup1)
    items = mainaddon.compile_playable_podcast(playable_podcast)
    return items

if __name__ == '__main__':
    plugin.run()
