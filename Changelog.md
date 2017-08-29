## 1.3.3 (unreleased)
- Allow renaming samples during configuration
- Bugfix: rename classification method silva to sina

## 1.3.2
- Bugfixes:
  - rdp confidence setting
  - add metadata to rdp and blast biom files
- Report improvements:
  - UNITE citation
  - bbduk filtering
  - txt otutable download
  - otu fasta download
  
## 1.3.1
- improved the automatic method template in the report
- Allow more settings to be automatically defined in conf.py:
  -  read stitching method
  - clustering
  - annotation
  - reference database
  - primers
- minor bug fixes:
  - add conda config rdp
 -  taxonomy formatting stampa
- Download and reformat UNITE database for use with STAMPA

## 1.3
- Allow for automatic configuration of remote projects at EBI.
- Support for automatic testing using EBI data
-  Add config option to convert to Casava 1.8 format
-  Add step to filter PhiX reads and adapter traces
-  Add (optional) step to remove remaining barcodes from reads
-  Allow to process unidirectional (or only forward) sequences when using the `mergepairs == none` option
-  Support extraction and classification of ITS reads
- Add 3 new method for taxonomy classification:
  - Add step to classify with pre-trained RDP database (for example UNITE for ITS)
  - Add STAMPA (vsearch) classification method
  - Add blast classification with lca option 
-  Use conda to install Sina (with bugfix)
- Add Swarm clustering method
- Automatically download SILVA database for STAMPA and Sina and also trim the database with given primers for STAMPA
- Improved generation of config file with `conf.py`
  - added command line options
  - automatically generate a `metadata.txt` template 
- Improved the report with a method part with references (bibtex)

## 1.2
- Initial support for a report rule

## 1.1
- Add support for automatically generated config files

## 1.0
- First release