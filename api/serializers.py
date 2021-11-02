from rest_framework import serializers

from .models import PackageRelease, Project
from .pypi import version_exists, latest_version

from rest_framework.renderers import JSONRenderer

class PackageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PackageRelease
        fields = ["name", "version"]
        extra_kwargs = {"version": {"required": False}}    

    def validate(self, data):

        if latest_version(data["name"]) == "None":        
            raise serializers.ValidationError()
            return                      

        if "version" in data.keys():               
            v_exists = version_exists(data["name"], data["version"])
            if v_exists == False:
                raise serializers.ValidationError()
                return            
        else:
            data["version"] = latest_version(data["name"])                 
        
        return data


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["name", "packages"]

    packages = PackageSerializer(many=True)  

    def create(self, validated_data):
        packages = validated_data["packages"]               

        projeto = Project(name=validated_data["name"])
        projeto.save()

        packageNames = []
        for pack in packages:
            if pack["name"] in packageNames:
                raise serializers.ValidationError()
                return
            packageNames.append(pack["name"])
            

        for pack in packages:
            package = PackageRelease(name=pack["name"], version=pack["version"], project=projeto)
            package.save()      
        
        return projeto
