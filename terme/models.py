from django.db import models
from django.utils.encoding import python_2_unicode_compatible

@python_2_unicode_compatible
class Client(models.Model):
  nom_client = models.CharField(max_length=84)
  
  def __str__(self):
    return self.nom_client
  
class Domaine(models.Model):
  nom_domaine = models.CharField(max_length=84)
  client = models.ForeignKey(Client)

  def __str__(self):
    return self.client.nom_client + '|' + self.nom_domaine

class Tag(models.Model):
  nom_tag = models.CharField(max_length=84)

  def __str__(self):
    return '[ ' + self.nom_tag + ' ]'

class TermeAn(models.Model):
  terme = models.CharField(max_length=84)
  definition = models.TextField(null=True)
  note = models.TextField(null=True)
  domaine = models.ForeignKey(Domaine)
  
  def __str__(self):
    return '[ ' + self.terme + ' ]'
 	
class Contexte(models.Model):
  contexte = models.CharField(max_length=84)
  note = models.TextField()

  def __str__(self):
    return '[ ' + self.contexte + ' ]'

class TermeFr(models.Model):
  terme = models.CharField(max_length=84, default='')
  definition = models.TextField(null=True)
  note = models.TextField(null=True)
  contexte = models.ForeignKey(Contexte)
  source = models.CharField(max_length=300,null=True)
  termeAn = models.ForeignKey(TermeAn)
  
  def __str__(self):
    return '[ ' + self.terme + '/' + self.termeAn.terme + ' (' + self.contexte.contexte + ') ]'
	
