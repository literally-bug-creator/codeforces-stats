from collections import defaultdict
from datetime import date

def filter_by_tags(submissions):
    tag_dict = defaultdict(list)

    for submission in submissions:
        for tag in submission.tags:
            tag_dict[tag].append(submission)

    return dict(tag_dict)


def filter_by_rating(submissions):
    rating_dict = defaultdict(list)

    for submission in submissions:
        if submission.rating is not None:
            rating_dict[submission.rating].append(submission)

    return dict(rating_dict)

def filter_by_verdict(submissions):
    verdict_dict = defaultdict(list)

    for submission in submissions:
        if submission.verdict == "OK":
            verdict_dict["OK"].append(submission)
        else:
            verdict_dict["NOT_OK"].append(submission)

    return dict(verdict_dict)


def filter_by_time(submissions, start_time, end_time):
    return [submission for submission in submissions if start_time <= submission.time <= end_time]


def get_rating_info(submissions, start_time, end_time=date.today()):
    submissions = filter_by_verdict(submissions)["OK"]
    submissions = filter_by_time(submissions, start_time, end_time)
    filtered_by_rating = filter_by_rating(submissions)

    return filtered_by_rating


def get_tags_info(submissions, start_time, end_time=date.today()):
    submissions = filter_by_verdict(submissions)["OK"]
    submissions = filter_by_time(submissions, start_time, end_time)
    filtered_by_tags = filter_by_tags(submissions)

    return filtered_by_tags


def get_tag_info(submissions, tag, start_time, end_time=date.today()):
    submissions = filter_by_verdict(submissions)
    ok_submissions, not_ok_submissions = submissions["OK"], submissions["NOT_OK"]
    tag_submissions_ok = filter_by_tags(ok_submissions)[tag]
    filtered_tag_submissions = filter_by_time(tag_submissions_ok, start_time, end_time)
    filtered_tag_submissions = filter_by_rating(filtered_tag_submissions)


    return filtered_tag_submissions

