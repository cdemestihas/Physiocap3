# -*- coding: utf-8 -*-
"""
/***************************************************************************
 Physiocap_var_exception
                                 A QGIS 3 plugin

 Le module Exception contient les variables et les définitions des exceptions
                             -------------------
        begin                : 2015-11-04
        git sha              : $Format:%H$
        email                : jean@jhemmi.eu
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 * Physiocap plugin créé par jhemmi.eu et CIVC est issu de :               *
 *- PSPY : PHYSIOCAP SCRIPT PYTHON VERSION 8.0 10/11/2014                  *
 *   CREE PAR LE POLE TECHNIQUE ET ENVIRONNEMENT DU CIVC                   *
 *   MODIFIE PAR LE CIVC ET L'EQUIPE VIGNOBLE DE MOËT & CHANDON            *
 *   AUTEUR : SEBASTIEN DEBUISSON, MODIFIE PAR ANNE BELOT ET MANON MORLET  *
 *   Physiocap plugin comme PSPY sont mis à disposition selon les termes   *
 *   de la licence Creative Commons                                        *
 *   CC-BY-NC-SA http://creativecommons.org/licenses/by-nc-sa/4.0/         *
 *- Plugin builder et QGIS 3 API et à ce titre porte aussi la licence GNU    *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *   http://www.gnu.org/licenses/gpl-2.0.html                              *
 *                                                                         *
***************************************************************************/
"""
import os 
import platform

# ###########################
# VARIABLES GLOBALES
# ###########################

# Ces variables sont nommées en Francais par compatibilité avec la version physiocap_V8
# Pour reconnaitre si Windows ou Linux
MACHINE = platform.system()
if MACHINE == "Linux":
    LE_MODE_PROD = "NO"
else:
    LE_MODE_PROD = "YES"
    
# TODO: Supprimer en Prod
#LE_MODE_PROD = "NO"

# En prod CENTROIDES vaut NO
CENTROIDES = "NO"  # CENTROIDES YES est pour voir les centroides dans la synthese
# Listes de valeurs pour la trace
TRACE_TOUT = "Traces complètes"
TRACE_MINI = "Traces minimales"
TRACE_PAS  = "Pas de trace"
MODE_TRACE = [ TRACE_TOUT,  TRACE_MINI, TRACE_PAS]
TRACE_INTRA  = "Intra"
TRACE_TOOLS  = "Tools"
TRACE_SEGMENT  = "Segment"
TRACE_SEGMENT_DECOUPES  = "Découpe"
TRACE_PG  = "POSTGRES"

REPERTOIRE_DONNEES_BRUTES = "Choisissez votre chemin"
PHYSIOCAP_NOM = "Physiocap"
PHYSIOCAP_NOM_3 = "Physiocap3"
PHYSIOCAP_UNI = u"\u03D5"
PHYSIOCAP_WARNING = u"\u26A0"
PHYSIOCAP_INFO = u"\U0001F6C8"
PHYSIOCAP_STOP = u"\U0001F6AB"
PHYSIOCAP_2_ETOILES = "**"
PHYSIOCAP_2_EGALS = "=="
PHYSIOCAP_LOG_ERREUR = PHYSIOCAP_WARNING + " " + PHYSIOCAP_UNI + " Erreurs"

# Test de robustesse de la gestion des unicodes
PHYSIOCAP_TEST1 = "ȧƈƈḗƞŧḗḓ ŧḗẋŧ ƒǿř ŧḗşŧīƞɠ"
PHYSIOCAP_TEST2 = "ℛℯα∂α♭ℓℯ ♭ʊ☂ η☺т Ѧ$☾ℐℐ"
PHYSIOCAP_TEST3 = "¡ooʇ ןnɟǝsn sı uʍop-ǝpısdn"
PHYSIOCAP_TEST4 = "Moët"
POSTGRES_NOM = "postgres"

SEPARATEUR_ ="_"
NOM_PROJET = "PHY" + SEPARATEUR_ # + PHYSIOCAP_TEST4 + SEPARATEUR_

FORMAT_VECTEUR = [ "ESRI Shapefile"] # POSTGRES_NOM] # "memory"]
FORMAT_VECTEUR_V3 = [ "ESRI Shapefile"] #,  "memory"] # POSTGRES_NOM] # "memory"]

# Répertoires des sources et de concaténation en fichiers texte
FICHIER_RESULTAT = "resultat.txt"
REPERTOIRE_SOURCES = "fichiers_sources"
SUFFIXE_BRUT_CSV = SEPARATEUR_ + "RAW.csv"
EXTENSION_MID = "*.MID"
NB_VIRGULES = 58

REPERTOIRE_TEXTES = "fichiers_texte"
REPERTOIRE_TEXTES_V3 = "csv"
# Pour histo
REPERTOIRE_HELP = os.path.join( os.path.dirname(__file__),"help")

FICHIER_HISTO_NON_CALCULE = os.path.join( REPERTOIRE_HELP, 
    "Histo_non_calcule.png")
SUFFIXE_HISTO = ".png"
REPERTOIRE_HISTOS = "histogrammes"
FICHIER_HISTO_SARMENT = "histogramme_SARMENT_RAW" + SUFFIXE_HISTO
FICHIER_HISTO_DIAMETRE = "histogramme_DIAMETRE_RAW"  + SUFFIXE_HISTO
FICHIER_HISTO_DIAMETRE_FILTRE = "histogramme_DIAM_FILTERED" +  SUFFIXE_HISTO

REPERTOIRE_SHAPEFILE = "shapefile"
REPERTOIRE_SHAPEFILE_V3 = "vecteur"
REPERTOIRE_RASTER_V3 = "raster"

EXTENSION_CSV = ".csv"
EXTENSION_SHP = ".shp"
EXTENSION_PRJ = ".prj"
EXTENSION_RASTER = ".tif"
EXTENSION_RASTER_SAGA_SANS_POINT = "sdat"
EXTENSION_RASTER_SAGA = "." + EXTENSION_RASTER_SAGA_SANS_POINT

EXTENSION_QML = ".qml"

EXTENSION_POUR_ZERO_V2 = SEPARATEUR_ + "0"
# Nom plus explicite pour V3
EXTENSION_SANS_ZERO= SEPARATEUR_ + "SANS_0"
EXTENSION_POUR_ZERO = SEPARATEUR_ + "AVEC_0"
EXTENSION_ZERO_SEUL = SEPARATEUR_ + "0_SEUL"

# SRC trouve dans EPSG
PROJECTION_L93 = "L93"
PROJECTION_GPS = "GPS"
PROJECTION_CC45 = "L93-CC45"

EPSG_NUMBER_L93 = 2154
EPSG_NUMBER_GPS = 4326
EPSG_NUMBER_CC45 = 3945
EPSG_TEXT_L93 = "EPSG:"+str(EPSG_NUMBER_L93)
EPSG_TEXT_GPS = "EPSG:"+str(EPSG_NUMBER_GPS)
EPSG_TEXT_CC45 = "EPSG:"+str(EPSG_NUMBER_CC45)
SPHEROID_L93 = "GRS80" #"GRS_1980"
SPHEROID_GPS = "WGS84" # "WGS_1984"
SPHEROID_CC45 = "GRS80" 
LISTE_EPSG=[      EPSG_NUMBER_L93, EPSG_NUMBER_GPS, EPSG_NUMBER_CC45]
LISTE_PROJECTION=[PROJECTION_L93,  PROJECTION_GPS,  PROJECTION_CC45]

# FICHIER .prj
EPSG_DESCRIPTION_L93 = 'PROJCS["RGF93 / Lambert-93", \
GEOGCS["RGF93",DATUM["D_RGF_1993", \
SPHEROID["GRS_1980",6378137,298.257222101]], \
PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]], \
PROJECTION["Lambert_Conformal_Conic"], \
PARAMETER["standard_parallel_1",49], \
PARAMETER["standard_parallel_2",44], \
PARAMETER["latitude_of_origin",46.5], \
PARAMETER["central_meridian",3], \
PARAMETER["false_easting",700000], \
PARAMETER["false_northing",6600000],UNIT["Meter",1]]'

EPSG_DESCRIPTION_GPS =  'GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984", \
SPHEROID["WGS_1984",6378137,298.257223563]], \
PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]]'

EPSG_DESCRIPTION_CC45 = 'PROJCS["RGF93 / CC45", \
GEOGCS["RGF93",DATUM["D_RGF_1993", \
SPHEROID["GRS_1980",6378137,298.257222101]], \
PRIMEM["Greenwich",0],UNIT["Degree",0.017453292519943295]], \
PROJECTION["Lambert_Conformal_Conic"], \
PARAMETER["standard_parallel_1",44.25], \
PARAMETER["standard_parallel_2",45.75], \
PARAMETER["latitude_of_origin",45], \
PARAMETER["central_meridian",3], \
PARAMETER["false_easting",1700000], \
PARAMETER["false_northing",4200000],UNIT["Meter",1]]'

# Champ des INFO DES SEGMENT FILTRE
DATE_DEBUT = "Date debut"
DATE_FIN = "Date fin"
NUM_SEG = "Numéro segment"
NOMBRE = "Longueur segment"
DERIVE = "Derive moyenne"
PDOP = "Pdop moyen"
GID_TROU = "Points manquants vs précedent"
GID_GARDE = "Points gardés"
GID_SANS_MESURE = "Points du segment sans mesure"

# Inter PARCELLAIRE
#SHAPE_CONTOURS = '/home/jhemmi/Documents/GIS/SCRIPT/QGIS/PhysiocapAnalyseur/data Cap/Contour.shp'
SEPARATEUR_NOEUD = "~~"
NOM_MOYENNE = SEPARATEUR_ + "MOYENNE" + SEPARATEUR_
VIGNETTES_INTER = "INTER_PARCELLAIRE"
NOM_POINTS = SEPARATEUR_ + "POINTS"
NOM_SEGMENTS = SEPARATEUR_ + "SEGMENTS"
NOM_SEGMENTS_DETAILS = NOM_SEGMENTS + SEPARATEUR_ + "BRISES"
NOM_INTER = SEPARATEUR_ + "INTER"

CONSOLIDATION = "CONSOLIDATION"

# Intra PARCELLAIRE
if MACHINE == "Linux":
    MON_TEMP="/tmp"
else:
    # MON_TEMP="C:\\Utilisateurs\\Utilisateur\\AppData\\Local\\Temp"
    MON_TEMP="C:/Users/Utilisateurs/AppData/Local/Temp"
    
VIGNETTES_INTRA = "INTRA_PARCELLAIRE"
NOM_INTRA = SEPARATEUR_ + "INTRA"
REPERTOIRE_RASTERS = "INTRA_PARCELLAIRE"
ATTRIBUTS_INTRA = ["DIAM", "NBSARM", "BIOM"]
ATTRIBUTS_INTRA_DETAILS = ["NBSARMM2", "NBSARCEP","BIOMM2", "BIOMGM2", "BIOMGCEP"]
# TODO: si GDAL & version 3 si ces index n'ont pas bougé avec les nouveau attributs de V3
ATTRIBUTS_INTRA_INDEX = {"DIAM" : 4 ,"NBSARM" : 3 ,"BIOM" : 5,  "NBSARMM2":6, "NBSARCEP":7,"BIOMM2":8, "BIOMGM2":9, "BIOMGCEP":10}
CHEMIN_TEMPLATES = [ "modeleQgis/V3", "project_templates/Physiocap3"]

# Exceptions Physiocap à partir de 30 erreurs sur un fchier mid
TAUX_LIGNES_ERREUR= 30

# ###########################
# Exceptions Physiocap
# ###########################
class physiocap_exception( BaseException):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)
    
class physiocap_exception_rep( physiocap_exception):
    pass
class physiocap_exception_fic( physiocap_exception):
    pass
class physiocap_exception_csv( physiocap_exception):
    pass
class physiocap_exception_err_csv( physiocap_exception):
    pass
class physiocap_exception_trop_err_csv( physiocap_exception):
    pass
class physiocap_exception_mid( physiocap_exception):
    pass
class physiocap_exception_no_mid( physiocap_exception):
    pass
class physiocap_exception_stop_user( physiocap_exception):
    pass  
class physiocap_exception_params( physiocap_exception):
    pass

# INTRA
class physiocap_exception_interpolation( physiocap_exception):
    pass
class physiocap_exception_vignette_exists( physiocap_exception):
    pass
class physiocap_exception_points_invalid( physiocap_exception):
    pass
class physiocap_exception_calcul_segment_invalid( physiocap_exception):
    pass
class physiocap_exception_segment_invalid( physiocap_exception):
    pass
class physiocap_exception_no_processing( physiocap_exception):
    pass
class physiocap_exception_no_saga( physiocap_exception):
    pass
class physiocap_exception_project_contour_incoherence( physiocap_exception):
    pass
class physiocap_exception_project_point_incoherence( physiocap_exception):
    pass
class physiocap_exception_windows_saga_ascii( physiocap_exception):
    pass
class physiocap_exception_windows_value_ascii( physiocap_exception):
    pass
class physiocap_exception_pg( physiocap_exception):
    pass

