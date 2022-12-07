from GitRecon import github_recon


def github_user_recon(username):
    github_user_info = github_recon.obtain_profile_info(username)
    github_recon.extract_orgs(username)
    github_user_keys = github_recon.obtain_keys(username)
    github_recon.extract_events_leaks(username)
    github_recon.validate_leaked_emails(github_recon.emails_list, github_user_info)
    return github_user_info, github_user_keys


def create_github_json_output(user_data, keys):
    json_output = {}
    json_output['username'] = user_data['login']
    json_output['name'] = user_data['name']
    json_output['id'] = user_data['id']
    json_output['avatar_url'] = user_data['avatar_url']
    json_output['orgs'] = []
    if user_data['email']:
        json_output['email'] = user_data['email']
    if user_data['location']:
        json_output['location'] = user_data['location']
    if user_data['bio']:
        json_output['bio'] = user_data['bio']
    if user_data['company']:
        json_output['company'] = user_data['company']
    for org in github_recon.orgs_list:
        json_output['orgs'].append(org)
    if user_data['blog']:
        json_output['blog'] = user_data['blog']
    if user_data['gravatar_id']:
        json_output['gravatar_id'] = user_data['gravatar_id']
    if user_data['twitter_username']:
        json_output['twitter_username'] = user_data['twitter_username']
    json_output['followers'] = user_data['followers']
    json_output['following'] = user_data['following']
    json_output['created_at'] = user_data['created_at']
    json_output['updated_at'] = user_data['updated_at']
    json_output['leaked_emails'] = []
    for email in github_recon.valid_emails:
        json_output['leaked_emails'].append(email)
    json_output['keys'] = []
    if keys:
        for key in keys:
            data = {'id': str(key['id']), 'key': str(key['key'])}
            json_output['keys'].append(data)
    return json_output


def gitrecon(username):
    user_info, keys = github_user_recon(username)
    return create_github_json_output(user_info, keys)
