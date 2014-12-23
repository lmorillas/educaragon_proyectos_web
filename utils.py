# coding: utf-8

'''
"url": "http://www.educaragon.org/impresos/formato9/formato9_ficha.asp?idTabla=409&idTipo=11&pag=11",
        "curso": ["2004/2005"],
        "centro": ["C.P. Tio Jorge de Zaragoza"],
        "coord": ["M\u00aa Vicenta Ca\u00f1ada Vicente"],
        "temas": ["Atenci\u00f3n a la Diversidad"],
        "label": ["PI/05/61 Un paso adelante hacia la integraci\u00f3n"]
        '''

claves = "curso centro coord temas label".split()

def uno(dato):
    for k in claves:
        _tmp = dato[k]
        if len(_tmp) > 1:
            print 'cambio', k
            dato[k] = _tmp[0]
    return dato



def cambia(dato):
    mal =  ['06/07', '07/08', '2009-2010', '2009 - 2010', '2010/20211', '20210/2011',
    '208/2009', '209-2010', '210/2011', '202010/2011', '2003/204', '2003-2004']
    bien = "2006/2007 2007/2008 2009/2010  2009/2010  2010/2011 2010/2011  2008/2009 2009/2010 2010/2011 2010/2011 2003/2004 2003/2004".split()
    corregir = dict(zip(mal, bien))
    for k in corregir:
        dato = dato.replace(k, corregir.get(k))
    return dato





