from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods
from django.contrib.auth import authenticate, login

from musicroom.common import apiRespond
from musicroom.models import User


@require_http_methods(["POST"])
def main(request):
    if request.user.is_authenticated:
        if "id" in request.POST:
            try:
                target_user = User.get_by_id(request.POST["id"])
            except:
                return apiRespond(400, msg="User does not exists")
            else:
                try:
                    friend = request.user.make_friend(target_user)
                except:
                    return apiRespond(400, msg='Already a friend or requested')
                else:
                    print(friend)
                    return apiRespond(201, msg='ok')
        else:
            return apiRespond(400, msg='id missing')
    else:
        # user is already logged in, redirect to root
        return apiRespond(401, msg='User not logged in')
