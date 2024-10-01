# TITLE
Last updated on [9/17/2024] by [Tyler Wade].

| Start Date | End Date | Contributors | Informed Stakeholders |
| ---------- | -------- | ------------ | --------------------- |
| 08/14/2024 |09/05/2024|  Tyler Wade  | Alicia Deletich       |                       |

# Overview
## Problem Statement
There are a number of finding aids in the YCBA-RBM ASpace repository that have AOs including bold tags/titles. Could these be removed via API

## Goals
 -Identify records in YCBA-RBM with <emph> in title
 
-Create/edit spreadsheet with updated titles

-Update titles

# Background
N/A


# Process

-see [ycba_title_update/get_ycba_emph_tags_titles.sql], [ycba_title_update/update_title.py]

-utilized 'get_ycba_emph_tags_titles.sql' SQL query that counts the number of records within the YCBA-RBM Aspace repositiory that have Archival objects with <emph> tags in title.

-Created a csv spreadsheet with a list of all the Archival objects that have <emph> tags/titles

-Update <emph> tags/titles using 'update_title.py' script


# Notes

| Date | Highlight | Notes |
| ---- | --------- | ----- |
<<<<<<< HEAD
|08/14/2024|Introduction to Project|Alicia Detelich introduced this project briefly as my second task/project.|
|08/22/2024|Meeting|Asked Alicia Detelich about 'update_title.py' script, how it works and things I can try to make it work.|
|08/29/2024|Meeting|Finally got script to work correctly and recived permission to update <emph> tags in Aspace production instance.|
|09/05/2024|Meeting| project/task completed.|
=======
|08/14/2024|Introduction to Project|Alicia Detelich introduced this project briefly as my second task/project.

|08/22/2024|Meeting|Asked Alicia Detelich about 'update_title.py' script, how it works and things I can try to make it work.

|08/29/2024|Meeting|Finally got script to work correctly and recived permission to update <emph> tags in Aspace production instance.

|09/05/2024|Meeting| bold tags/titles project/task completed.
>>>>>>> 2fe82fcabfe1e25bcc18862b66ba8d74f4be7bfa


# Review

## Data Details
|uri|                                            |title|

-|/repositories/2/archival_objects/3848|  <emph>Letter from Ruvigny de Cosne to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3849|  <emph>Letter from Ruvigny de Cosne to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3850|  <emph>Letter from Jean Desbiey to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3851|  <emph>Letter from de Monsert to Chauvigny (?)</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3852|  <emph>Letter from William Heriot Dundas to unknown</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3853|  <emph>Letter from John Ford and Simon Peter Cruise to Dorothy Hooper</emph> :  manuscript copy|

-|/repositories/2/archival_objects/3854|  <emph>Letter from John Ford to George Whatley</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3855|  <emph>Letter to John Ford Esqr</emph> : manuscript |

-|/repositories/2/archival_objects/3856|  <emph>Translation of a letter from the Dey of Algiers to Secy. Pitt, recd. from Algier with the original, delivd. May 29th 1761 by Omar Effendi</emph> : manuscript |

-|/repositories/2/archival_objects/3857|  <emph>Mr. Butler's translation of a letter from the Dey of Algier to Mr. Secry. Pitt, delivered May 29th, 1761, by Omar Effendi</emph> : manuscript|

-|/repositories/2/archival_objects/3858|  <emph>Mr. Aspinwall's translation of the Dey of Algier's letter to the King; Omar Effendi's credentials, delivered June 3d. 1761</emph> : manuscript |

-|/repositories/2/archival_objects/3859|  <emph>Mr. Butler's translation of the Dey of Algier's letter to the King; Omar Effendi's credentials. Delivered June 8th, 1761</emph> : manuscript |

-|/repositories/2/archival_objects/3860|  <emph>Letter from the Dey of Algiers to Stanhope Aspinwall</emph> : manuscript |

-|/repositories/2/archival_objects/3861|  <emph>Copy of His Majesty's letter to the Dey of Algiers. Augt. 18 1761</emph> : manuscript |

-|/repositories/2/archival_objects/3862|  <emph>Letter from Stanhope Aspinwall to Joseph Richardson</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3863|  <emph>Copy of a letter from His Majesty to the Dey of Algier. Feby. 26th, 1762</emph> : manuscript|

-|/repositories/2/archival_objects/3864|  <emph>Copy of a letter from the Earl of Egremont to the Dey of Algiers. Feb. 26th, 1762</emph> : manuscript |

-|/repositories/2/archival_objects/3865|  <emph>Letter from George Whatley to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3866|  <emph>Letter from George Whatley to unknown</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3867|  <emph>Letter from Choiseul to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3868|  <emph>Copy of a letter from George III to the Dey of Algier</emph> : manuscript signed|

-|/repositories/2/archival_objects/3869|  <emph>Letter from Joseph Richardson to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3870|  <emph>Copies of letters to Simon Peter Cruise</emph> : manuscript copies|

-|/repositories/2/archival_objects/3871|  <emph>Letter from Guillaume-Léon du Tillot, probably to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3872|  <emph>Letter from John Dick to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3873|  <emph>Letter from the Earl of Egremont to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3874|  <emph>Letter from Joseph Richardson to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3875|  <emph>Letter from Egremont to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3876|  <emph>Letter from Egremont to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3877|  <emph>Letter from Alexander Mackenzie to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3878|  <emph>Letter from David Williams to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3879|  <emph>Letter from William Howe to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3880|  <emph>Letter from Horace Mann, presumably to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3881|  <emph>Letter from Pietro Giovanni Capriata to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3882|  <emph>Letter from Peter Templeman to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3883|  <emph>Letter from Egremont to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3884|  <emph>Letter from M. Stephenson to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3885|  <emph>Letter from John Dick to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3886|  <emph>Letter from William Howe to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3887|  <emph>Letter from unknown to James Bruce</emph> : manuscript |

-|/repositories/2/archival_objects/3888|  <emph>Letter from Alexander Brown to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3889|  <emph>Letter from Guillaume-Léon Du Tillot to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3890|  <emph>Letter from Egremont to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3891|  <emph>Letter from John Dick to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3892|  <emph>Letter from Robert Wood to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3893|  <emph>Letter from Joseph Richardson to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3894|  <emph>Letter from unknown to James Bruce</emph> :  manuscript |

-|/repositories/2/archival_objects/3895|  <emph>Letter from Lefroy and Charron to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3896|  <emph>Letter from Joseph Basquans to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3897|  <emph>Letter from John Udny to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3898|  <emph>Letter from Raphael Jacob Bussara to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3899|  <emph>Letter from C.W. Tonyn to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3900|  <emph>Letter from Richard Dacres to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3901|  <emph>Letter from James Bruce to John Dick, Esq.</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3902|  <emph>Letter from Simon Peter Cruise to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3903|  <emph>Letter from Simon Peter Cruise to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3904|  <emph>Letter from Giovani Stefanopoli to unknown</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3905|  <emph>Letter from Simon Bava (?) to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3906|  <emph> Letter from Aniello Gargiulo to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3907|  <emph>Letter  from Jean Louis Ployard to James Bruce </emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3908|  <emph>Letter from William Gerard Hamilton to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3909|  <emph>Letter from Alexander Mackenzie to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3910|  <emph>Letter from Andrew Drummond to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3911|  <emph>Letter from George Whatley to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3912|  <emph>Copies of letters to James Bruce and copy of a petition</emph> : manuscript copies|

-|/repositories/2/archival_objects/3913|  <emph>Letter from Robert Wood to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3914|  <emph>Letter from Alexander Mackenzie to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3915|  <emph>Letter from Hamilton Lambart to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3916|  <emph>Letter from George Pitt to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3917|  <emph>Copies of letters from Charles Gordon to James Bruce</emph> : autograph manuscripts signed|

-|/repositories/2/archival_objects/3918|  <emph>Letter from John Mackenzie to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3919|  <emph>Letter from Richard Dacres to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3920|  <emph>Copy of a letter from Mackenzie and Hayes(?) to James Bruce(?)</emph> : manuscript|

-|/repositories/2/archival_objects/3921|  <emph>Letter from Mackenzie and Hayes to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3922|  <emph>Letter from John Higgins to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3923|  <emph>Letter from Simon Peter Cruise to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3924|  <emph>Letter from R. Muller to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3925|  <emph>Letter from unknown to James Bruce</emph> : manuscript|

-|/repositories/2/archival_objects/3926|  <emph>Letters from Jean Louis Ployart to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3927|  <emph>Letter from the Earl of Egremont to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3928|  <emph>Letter from Lord Halifax to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3929|  <emph>Letter from James Bruce to unknown</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3930|  <emph>Letter from R. Muller to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3931|  <emph>Letter from Domenico Hernando to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3932|  <emph>Letter from Dunk Halifax to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3933|  <emph>Letter from Kaggi Demetrio Marcachi to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3934|  <emph>Letter from William Hamilton to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3935|  <emph>Letter from Peter Charron to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3936|  <emph>Letter from Robert Brown to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3937|  <emph>Letter from Lefroy & Charron to James Bruce, with two invoices</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3938|  <emph>Letter from Peter Charron to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3939|  <emph>Letters from Jean Louis Ployard to James Bruce</emph> : manuscripts signed|

-|/repositories/2/archival_objects/3940|  <emph>Letter from R. Muller to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3941|  <emph>Letter from Dunk Halifax to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3942|  <emph>Letter from William Hamilton to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3943|  <emph>Copies of letters from Jean Louis Ployard to James Bruce</emph> : manuscripts signed|

-|/repositories/2/archival_objects/3944|  <emph>Copy of a letter from unknown to James Bruce</emph> : manuscript|

-|/repositories/2/archival_objects/3945|  <emph>Letter from John Dick to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3946|  <emph>Letter from Captain Nicola Paleologo to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3947|  <emph>Letters to James Bruce</emph> : manuscripts|

-|/repositories/2/archival_objects/3948|  <emph>Letter from Joseph Curboy to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3949|  <emph>Letter from George Chalmers to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3950|  <emph>Letter from James Bruce to Sir Richard Lyttelton (?)</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3951|  <emph>Letter from unknown to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3952|  <emph>Letter from Dunk Halifax to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3953|  <emph>Letter from Lefroy & Charron to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3954|  <emph>Letter from Andrew Richard Den to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3955|  <emph>Letter from Thomas Harrison to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3956|  <emph>Copy of a letter from Thomas Harrison to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3957|  <emph>Letter from James Johnston to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3958|  <emph>Letter from Robert Sorbes to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3959|  <emph>Letter from Jean Louis Ployard to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3960|  <emph>Letter from Mackenzie & Hays to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3961|  <emph>Letter from George Pitt to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3962|  <emph>Letter from Simon Forbes to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3963|  <emph>Letter from Theodore Alexiano to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3964|  <emph>Letter from Prince Benedetto Giustiniani to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3965|  <emph>Letter from Carlo Fogliata to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3966|  <emph>Letter from R. Muller to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3967|  <emph>Letter from the Earl of Halifax to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3968|  <emph>Letter from Robert Strange to Jean Louis Ployard</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3969|  <emph>Letter from Aron Narboni to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3970|  <emph>Letter from Jean Louis Ployard to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3971|  <emph>Letter from John Udny to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3972|  <emph>Letter from unknown to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3973|  <emph>Letter from Barrington Taverner to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3974|  <emph>Letter from Joseph Richardson to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3975|  <emph>Letter from George Whatley to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3976|  <emph>Copy of a letter from George Whatley to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3977|  <emph>Copy of a letter from George Whatley to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3978|  <emph>Letter from George Whatley to Jean Louis Ployard</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3979|  <emph>Letter from Joseph Popham to Captain Hillary Le Pelley</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3980|  <emph>Letter from unknown to unknown</emph> : manuscript|

-|/repositories/2/archival_objects/3981|  <emph>Copy of a letter from George Whatley to Simon Peter Cruise</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3982|  <emph>Copy of a letter from unknown to James Bruce</emph> : manuscript|

-|/repositories/2/archival_objects/3983|  <emph>Letter from James Bruce to unknown</emph> : autograph manuscript|

-|/repositories/2/archival_objects/3984|  <emph>Letter from Captain James Johnston to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3985|  <emph>Letter from James Bruce to unknown</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3986|  <emph>Letter from James Bruce to unknown</emph> : manuscript|

-|/repositories/2/archival_objects/3987|  <emph>Letter from Constantino Stinca to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3988|  <emph>Letter from Giovanni Xeno to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3989|  <emph>Letter from Horace Mann to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3990|  <emph>Letter from Edward Clarke to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3991|  <emph>Letter from Joseph Richardson to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3992|  <emph>Letter from Ployard to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3993|  <emph>Letter from John Birkbeck to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3994|  <emph>Letter from Lefroy and Charron to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3995|  <emph>Letters from Lefroy and Charron to James Bruce</emph> : manuscripts|

-|/repositories/2/archival_objects/3996|  <emph>Letter from George Pitt to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/3997|  <emph>Letter from E. Brander to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3998|  <emph>Letter from Nicola Voverano to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/3999|  <emph>Letter from William Hamilton to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4000|  <emph>Letter from John Nightman to James Bruce</emph> : manuscript|

-|/repositories/2/archival_objects/4001|  <emph>Letter from Patrick Hays to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4002|  <emph>Letter from Patrick Hays to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4003|  <emph>Letter from Ployard to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4004|  <emph>Letter from George Fraser to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/4005|  <emph>Letter from Francesco Voverano to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4006|  <emph>Letter from Theodore Alexiano to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4007|  <emph>Copy of a letter from George Chalmers to James Bruce</emph> : manuscript|

-|/repositories/2/archival_objects/4008|  <emph>Letter from Robert Forbes to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/4009|  <emph>Letter from James Bruce to Unknown [George Halifax?]</emph> : autograph manuscript|

-|/repositories/2/archival_objects/4010|  <emph>Letter from James Bruce to Unknown [George Halifax?]</emph> : autograph manuscript|

-|/repositories/2/archival_objects/4013|  <emph>Letter from James Bruce to Unknown</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4014|  <emph>Letter from James Bruce to Paolo Colucci</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4015|  <emph>Letter from James Bruce to Paolo Colucci</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4016|  <emph>Letter from James Bruce to Unknown [Halifax?]</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4017|  <emph>Letter from George Chalmers to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4018|  <emph>Letter from Joseph Popham to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4019|  <emph>Letters from James Bruce to Unknown and Drummond & Co.</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4020|  <emph>Letter from Constantino Stinca to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4021|  <emph>Letter from R. Muller to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4022|  <emph>Letter from John Birkbeck to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4023|  <emph>Letters from Ployard to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4024|  <emph>Letters from Ployard to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4025|  <emph>Letter from Giovanni Stefanopoli to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4026|  <emph>Letter from James Bruce to Unknown [Halifax?]</emph> : autograph manuscript|

-|/repositories/2/archival_objects/4027|  <emph>Letter from Constantino Stinca to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4115|  <emph>Letter from Lefroy and Charron to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4116|  <emph>Letter from Angelo Dordenghi to Luigi Balugani</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4117|  <emph>Letter from Tho. Townshend to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4118|  <emph>Letter from Joseph Popham to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4119|  <emph>Letter from Kirkpatricks and Escott to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4120|  <emph>Letter from Giovanni Comata to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4121|  <emph>Letter from Giovanni Comata to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4122|  <emph>Letter from Giovanni Comata to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4123|  <emph>Letter from Giuseppe Chiesa to Luigi Balugani</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4124|  <emph>Letter from William Hamilton to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4125|  <emph>Letter from James Bruce to Unknown</emph>: autograph manuscript |

-|/repositories/2/archival_objects/4126|  <emph>Letter from Giovanni Comata</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4127|  <emph>Letter from Wombwell's Coxon and Wombwell to James Bruce</emph>: manuscript signed|

-|/repositories/2/archival_objects/4128|  <emph>Letter from John Dick to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4129|  <emph>Letter from Giovanni Comata to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4130|  <emph>Letter from Domenico Hernando to Unknown [James Bruce]</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4131|  <emph>Letter from [James Bruce] to [Lord Halifax]</emph>: autograph manuscript|

-|/repositories/2/archival_objects/4132|  <emph>Letter from Thomas Townshend to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4133|  <emph>Copy of a letter from Thomas Townshend to Archibald Cleveland</emph>: manuscript|

-|/repositories/2/archival_objects/4134|  <emph>Letter from Thomas Townshend to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4135|  <emph>Letter from Francesco Bichi to [James Bruce]</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4136|  <emph>Letter from James Dick to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4137|  <emph>Letter from Dunk Halifax to James Bruce</emph>: manuscript signed|

-|/repositories/2/archival_objects/4138|  <emph>Letter from Patrick MacKellar to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4139|  <emph>Letter from George Whatley to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4140|  <emph>Letter from Frederic Armano to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4141|  <emph>Letter from Lefroy and Charron to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4142|  <emph>Letter from James Bruce to Eric Brander</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4143|  <emph>Letters from Ployart to James Bruce</emph>: manuscripts|

-|/repositories/2/archival_objects/4144|  <emph>Letter from P. Lyons to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4145|  <emph>Letter from George Chalmers to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4146|  <emph>Letter from Anthony Seyel to Unknown</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4147|  <emph>Letter from Simon Peter Cruise to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4148|  <emph>Letter from Archibald Cleveland to James Bruce</emph>: manuscript signed|

-|/repositories/2/archival_objects/4149|  <emph>Letter from Archibald Cleveland to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4150|  <emph>Letter from Giuseppe Zapello to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4151|  <emph>Letter from Robert Kirke to [James Bruce]</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4152|  <emph>Letter from Giovanni Stefanopoli to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4153|  <emph>Letter from Archibald Cleveland to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4154|  <emph>Letter from James Bruce to [Archibald Cleveland]</emph>: autograph manuscript|

-|/repositories/2/archival_objects/4155|  <emph>Letter from Archibald Cleveland to [James Bruce]</emph>: autograph manuscript|

-|/repositories/2/archival_objects/4156|  <emph>Letter from Robert Kirke to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4157|  <emph>Letter from Andrew Lumisden to James Bruce</emph>: autograph manuscript|

-|/repositories/2/archival_objects/4158|  <emph>Letter from Robert Kirke to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4159|  <emph>Letter from Lefroy and Charron to James Bruce</emph>: autograph manuscript signed|

-|/repositories/2/archival_objects/4160|  <emph>Letter from Giovanni Xeno to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/4161|  <emph>Letter from Giovanni Xeno to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4162|  <emph>Letter from Giovanni Xeno to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4163|  <emph>Letter from George Lawrence to [James Bruce]</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4164|  <emph>Letter from Archibald Cleveland to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4166|  <emph>Letter from Thomas Seymour to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/4167|  <emph>Letter from James Bruce to [Lord Halifax]</emph> : autograph manuscript|

-|/repositories/2/archival_objects/4168|  <emph>Letter from Simon Peter Cruise to [Robert Kirke]</emph> : manuscript|

-|/repositories/2/archival_objects/4169|  <emph>Letter from Robert Kirke to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4170|  <emph>Letter from Robert Kirke to [James Bruce]</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4171|  <emph>Letters from James Bruce to Consul Kirke</emph> : autograph manuscripts signed|

-|/repositories/2/archival_objects/4172|  <emph>Letter from Robert Kirke to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4173|  <emph>Letter from Chore[?] to [James Bruce]</emph> : manuscript signed|

-|/repositories/2/archival_objects/4174|  <emph>Letter from Charles Gordon to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4175|  <emph>Letter from D.V. Servitore[?] to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4177|  <emph>Letter from V.D. Servitore and Gio. Percile[?] to Unknown</emph> : manuscript signed|

-|/repositories/2/archival_objects/4178|  <emph>Letter from Lefroy and Charron to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4179|  <emph>Letter from Giovanni Comata to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4180|  <emph>Letter from Charlie Gordon to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4181|  <emph>Letter from Isach Ser[?] to James Bruce</emph> : manuscript signed|

-|/repositories/2/archival_objects/4182|  <emph>Letter from Busnah[?] to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4183|  <emph>Letter from Gio DiGiano[?] to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4185|  <emph>Letter from Charles Gordon to James Bruce</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4186|  <emph>Letter from Gio. Giano to Unknown</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4190|  <emph>Letter from Giuseppe Crudli[?] to Luigi Balugani</emph> : autograph manuscript signed|

-|/repositories/2/archival_objects/4191|  <emph>Letter from [James Bruce] to Unknown</emph> : autograph manuscript|


## Communication
Name             | Position                                                      | Notes                                                                   |
|Alicia Detelich | Head of Special Collections Metadata Services in Beinecke     |Alicia Detelich gave advice and direction on how to complete project/task|

## Results
<emph> tag/title updates ran smoothly with no issues.

# References
N/A
