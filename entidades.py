from abc import ABC, abstractmethod

class Usuario(ABC):
  def __init__(self, Nome = None, NumeroMatricula = None, CPF = None, Tipo = None, EmailInstitucional = None):
    self.__Nome = Nome
    self.__NumeroMatricula = NumeroMatricula
    self.__CPF = CPF
    self.__Tipo = Tipo
    self.__EmailInstitucional = EmailInstitucional


  def setNome(self, Nome):
    self.__Nome = Nome
  def getNome(self):
    return self.__Nome


  def setNumeroMatricula(self, NumeroMatricula):
    self.__NumeroMatricula = NumeroMatricula
  def getNumeroMatricula(self):
    return self.__NumeroMatricula


  def setCPF(self, CPF):
    self.__CPF = CPF
  def getCPF(self):
    return self.__CPF


  def setTipo(self, Tipo):
    self.__Tipo = Tipo
  def getTipo(self):
    return self.__Tipo


  def setEmailInstitucional(self, EmailInstitucional):
    self.__EmailInstitucional = EmailInstitucional
  def getEmailInstitucional(self):
    return self.__EmailInstitucional


class Aluno(Usuario):
  def __init__(self, Nome = None, NumeroMatricula = None, CPF = None, Tipo = None, EmailInstitucional = None, Periodo=None, Curso=None, Coordenador=None):
    super().__init__(Nome=None, NumeroMatricula=None, CPF=None, Tipo=None, EmailInstitucional=None)
    self.__Periodo = Periodo
    self.__Curso = Curso
    self.__Coordenador = Coordenador


  def getCoordenador(self):
    return self.__Coordenador
  def setCoordenador(self, coordenador):
    self.__Coordenador = coordenador
  
  def getPeriodo(self):
    return self.__Periodo
  def setPeriodo(self,Periodo):
    self.__Periodo = Periodo


  def getCurso(self):
    return self.__Curso
  def setCurso(self,Curso):
    self.__Curso = Curso


class Adm(Usuario):
  def __init__(self, Nome = None, NumeroMatricula = None, CPF = None, Tipo = None, EmailInstitucional = None, Formacao=None, CargaHoraria=None):
    super().__init__(Nome=None, NumeroMatricula=None, CPF=None, Tipo=None, EmailInstitucional=None)
    self.__Formacao = Formacao
    self.__CargaHoraria = CargaHoraria


  def getFormacao(self):
    return self.__Formacao
  def setFormacao(self, Formacao):
    self.__Formacao = Formacao


  def getCargaHoraria(self):
    return self.__CargaHoraria  
  def setCargaHoraria(self,Periodo):
    self.__Periodo = Periodo

     

class Solicitacao:
  def __init__(self, MatriculaSolicitante = None | str, Data = None | str, DocumentoSolicitado = None | str, EncaminhadoPara = None | str | list, DocumentosNecessarios = list):
      self.__MatriculaSolicitante = MatriculaSolicitante
      self.__Data = Data
      self.__DocumentoSolicitado = DocumentoSolicitado
      self.__EncaminhadoPara = EncaminhadoPara
      self.__DocumentosNecessarios = DocumentosNecessarios


  def setDocumentosNecessarios(self, DocumentosNecessarios):
    self.__DocumentosNecessarios = DocumentosNecessarios
  def getDocumentosNecessarios(self):
    return self.__DocumentosNecessarios
  
  
  def setMatriculaSolicitante(self, MatriculaSolicitante):
    self.__MatriculaSolicitante = MatriculaSolicitante
  def getMatriculaSolicitante(self):
    return self.__MatriculaSolicitante


  def setData(self, Data):
    self.__Data = Data
  def getData(self):
      return self.__Data


  def setDocumentoSolicitado(self, DocumentoSolicitado):
      self.__DocumentoSolicitado = DocumentoSolicitado
  def getDocumentoSolicitado(self):
      return self.__DocumentoSolicitado


  def setEncaminhadoPara(self, EncaminhadoPara):
      self.__EncaminhadoPara = EncaminhadoPara
  def getEncaminhadoPara(self):
      return self.__EncaminhadoPara
