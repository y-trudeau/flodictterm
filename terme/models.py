from django.db import models

class Client(models.Model):
  nom_client = models.CharField(max_length=84)
  
  def __unicode__(self):
    return self.nom_client
  
class Domaine(models.Model):
  nom_domaine = models.CharField(max_length=84)
  client = models.ForeignKey(Client)

  def __unicode__(self):
    return self.client.nom_client + '.' + self.nom_domaine

class Tag(models.Model):
  nom_tag = models.CharField(max_length=84)

  def __unicode__(self):
    return '[ ' + self.nom_tag + ' ]'

class Terme(models.Model):
  terme_fr = models.CharField(max_length=84)
  terme_an = models.CharField(max_length=84)
  definition = models.TextField()
  domaine = models.ManyToManyField(Domaine)
  tag = models.ManyToManyField(Tag)
  
  def __unicode__(self):
    return '[ ' + self.terme_fr + ' / ' + self.terme_an + ' ]'

class Context(models.Model):
  source = models.CharField(max_length=300)
  context = models.TextField()


