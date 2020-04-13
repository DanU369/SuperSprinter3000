from flask import Flask, render_template, request, redirect

import data_handler

app = Flask(__name__)


@app.route('/')
def route_list():
    user_stories = data_handler.get_all_user_story()
    table_header = ['ID', 'Title', 'User Story', 'Acceptance Criteria', 'Business Value', 'Estimation', 'Status']
    return render_template('list.html', user_stories=user_stories, table_header=table_header)


@app.route('/story', methods=['GET', 'POST'])
def story():
    user_stories = data_handler.get_all_user_story()
    ids = []
    for story in user_stories:
        ids.append(story['id'])
    new_story = {}
    # when we submit the form with POST method we will have the string 'POST' in request.method
    if request.method == 'POST':
        if len(ids)==0:
            new_story['id'] = "0"
        else:
            new_story['id'] = str(int(max(ids)) + 1)
        new_story['title'] = request.form['title']
        new_story['user_story'] = request.form['user_story']
        new_story['acceptance_criteria'] = request.form['acceptance_criteria']
        new_story['business_value'] = request.form['business_value']
        new_story['estimation'] = request.form['estimation']
        new_story['status'] = data_handler.STATUSES[0]
        user_stories.append(new_story)
        data_handler.write_to_file(user_stories)
        return redirect('/')
    return render_template('story.html')


@app.route('/story/<story_id>', methods=['GET', 'POST'])
def edit_story(story_id=None):
    statuses = data_handler.STATUSES
    user_stories = data_handler.get_all_user_story()
    new_story = user_stories[int(story_id)]
    user_stories.remove(new_story)
    # when we submit the form with POST method we will have the string 'POST' in request.method
    if request.method == 'POST':
        new_story['id'] = story_id
        new_story['title'] = request.form['title']
        new_story['user_story'] = request.form['user_story']
        new_story['acceptance_criteria'] = request.form['acceptance_criteria']
        new_story['business_value'] = request.form['business_value']
        new_story['estimation'] = request.form['estimation']
        new_story['status'] = request.form['status']
        user_stories.insert(int(story_id),new_story)
        data_handler.write_to_file(user_stories)
        return redirect('/')
    return render_template('story.html' , story_id=story_id, new_story=new_story, statuses=statuses)


if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=8000,
        debug=True,
    )
