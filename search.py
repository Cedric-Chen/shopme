#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
from flask import Flask
from flask import render_template

#from config import app, app_debug, log_dir
#from www import url
from datamodel_test.business import model as Business
from datamodel_test.review import model as Review
from datamodel_test.user import model as User
from datamodel_test.hours import model as Hours
from datamodel_test.checkin import model as Checkin

# from datamodel.business import business
# from datamodel.review import review
# from datamodel.user import user
# from datamodel.hours import hours

app = Flask(__name__)

@app.route(u'/search')
def search():
    business = Business.get_business()
    review = Review.get_review()
    user = User.get_user()
    checkin = Checkin.get_checkin()

    # business = business.select()
    # review = review.select()
    # user = user.select()
    num_item = 10

    business_list = [business for i in range(num_item)]
    review_list = [review for i in range(num_item)]
    user_list = [user for i in range(num_item)]
    checkin_list = [checkin for i in range(num_item)]
    num_checkin_list = []
    for c in checkin_list:
        num_checkin_list.append(sum(list(c.values())))

    result_list = list()
    for idx in range(num_item):
        result = dict()
        result['business'] = business_list[idx]
        result['review'] = review_list[idx]
        result['user'] = user_list[idx]
        result['num_checkin'] = num_checkin_list[idx]
        result_list.append(result)

    return render_template(u'search.html',
                            result_list=result_list)


if __name__ == '__main__':
    app.run()
