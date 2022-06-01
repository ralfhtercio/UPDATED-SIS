BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "coursedata" (
	"course_id"	VARCHAR(10) NOT NULL,
	"course_name"	VARCHAR(100) NOT NULL,
	PRIMARY KEY("course_id")
);
CREATE TABLE IF NOT EXISTS "studentdata" (
	"stud_id"	VARCHAR(9) NOT NULL,
	"stud_name"	VARCHAR(100) NOT NULL,
	"stud_year"	VARCHAR(8),
	"stud_course_id"	VARCHAR(10),
	"stud_gender"	VARCHAR(6) NOT NULL,
	PRIMARY KEY("stud_id"),
	FOREIGN KEY("stud_course_id") REFERENCES "coursedata"("course_id") ON DELETE RESTRICT ON UPDATE CASCADE
);
INSERT INTO "coursedata" VALUES ('BS ANIMBIO','BACHELOR OF SCIENCE IN ANIMAL BIOLOGY');
INSERT INTO "coursedata" VALUES ('BS STAT','BACHELOR OF SCIENCE IN STATISTICS');
INSERT INTO "coursedata" VALUES ('BS CHEM','BACHELOR OF SCIENCE IN CHEMISTRY');
INSERT INTO "coursedata" VALUES ('BS PED','BACHELOR OF SCIENCE IN PHYSICAL EDUCATION');
INSERT INTO "coursedata" VALUES ('BS CS','BACHELOR OF SCIENCE IN COMPUTER SCIENCE');
INSERT INTO "coursedata" VALUES ('BSN','BACHELOR OF SCIENCE IN NURSING');
INSERT INTO "coursedata" VALUES ('BS CE','BACHELOR OF SCIENCE IN CIVIL ENGINEERING');
INSERT INTO "coursedata" VALUES ('BS MATH','BACHELOR OF SCIENCE IN MATHEMATICS');
INSERT INTO "coursedata" VALUES ('BS CHE','BACHELOR OF SCIENCE IN CHEMICAL ENGINEERING');
INSERT INTO "coursedata" VALUES ('BS METE','BACHELOR OF SCIENCE IN METALLURGICAL ENGINEERING');
INSERT INTO "coursedata" VALUES ('BS PHYSICS','BACHELOR OF SCIENCE IN PHYSICS');
INSERT INTO "coursedata" VALUES ('BS MARBIO','BACHELOR OF SCIENCE IN MARINE BIOLOGY');
INSERT INTO "coursedata" VALUES ('BS MICROBIO','BACHELOR OF SCIENCE IN MICROBIOLOGY');
INSERT INTO "coursedata" VALUES ('BSA','BACHELOR OF SCIENCE IN ACCOUNTANCY');
INSERT INTO "coursedata" VALUES ('AB ENGLISH','BACHELOR OF ARTS IN ENGLISH');
INSERT INTO "coursedata" VALUES ('BS PSYCH','BACHELOR OF SCIENCE IN PSYCHOLOGY');
INSERT INTO "coursedata" VALUES ('BA FILIPINO','BACHELOR OF ARTS IN FILIPINO');
INSERT INTO "coursedata" VALUES ('BA HISTORY','BACHELOR OF ARTS IN HISTORY');
INSERT INTO "coursedata" VALUES ('BA POLSCI','BACHELOR OF ARTS IN POLITICAL SCIENCE');
INSERT INTO "coursedata" VALUES ('BS CERE','BACHELOR OF SCIENCE IN CERAMIC ENGINEERING');
INSERT INTO "coursedata" VALUES ('BS COME','BACHELOR OF SCIENCE IN COMPUTER ENGINEERING');
INSERT INTO "coursedata" VALUES ('BS MECHE','BACHELOR OF SCIENCE IN MECHANICAL ENGINEERING');
INSERT INTO "coursedata" VALUES ('BS EE','BACHELOR OF SCIENCE IN ELECTRICAL ENGINEERING');
INSERT INTO "coursedata" VALUES ('BS ECE','BACHELOR OF SCIENCE IN ELECTRONICS AND COMMUNICATIONS ENGINEERING');
INSERT INTO "coursedata" VALUES ('BS PLANTBIO','BACHELOR OF SCIENCE IN PLANT BIOLOGY');
INSERT INTO "coursedata" VALUES ('BS BIODIV','BACHELOR OF SCIENCE IN BIODIVERSITY');
INSERT INTO "coursedata" VALUES ('BS ENVI ENG','BACHELOR OF SCIENCE IN ENVIRONMENTAL ENGINEERING');
INSERT INTO "coursedata" VALUES ('BS GENBIO','BACHELOR OF SCIENCE IN GENERAL BIOLOGY');
INSERT INTO "coursedata" VALUES ('BSED BIOLOGY','BACHELOR OF SECONDARY EDUCATION (BIOLOGY)');
INSERT INTO "coursedata" VALUES ('BSED CHEM','BACHELOR OF SECONDARY EDUCATION (CHEMISTRY)');
INSERT INTO "coursedata" VALUES ('BSBA MARKETING','BACHELOR OF SCIENCE IN BUSINESS ADMINISTRATION - MARKETING MANAGEMENT');
INSERT INTO "coursedata" VALUES ('BS IT','BACHELOR OF SCIENCE IN INFORMATION TECHNOLOGY');
INSERT INTO "coursedata" VALUES ('BS CA','BACHELOR OF SCIENCE IN COMPUTER APPLICATIONS');
INSERT INTO "coursedata" VALUES ('BSED PHYSICS','BACHELOR OF SECONDARY EDUCATION (PHYSICS)');
INSERT INTO "coursedata" VALUES ('BSED MAPEH','BACHELOR OF SECONDARY EDUCATION (MAPEH)');
INSERT INTO "coursedata" VALUES ('BSED TLE','BACHELOR OF SECONDARY EDUCATION (TLE)');
INSERT INTO "coursedata" VALUES ('BSED MATH','BACHELOR OF SECONDARY EDUCATION (MATHEMATICS)');
INSERT INTO "coursedata" VALUES ('BEED LANGUAGE EDUCATION','BACHELOR OF ELEMENTARY EDUCATION - LANGUAGE EDUCATION');
INSERT INTO "coursedata" VALUES ('BEED MATH','BACHELOR OF ELEMENTARY EDUCATION (MATHEMATICS)');
INSERT INTO "coursedata" VALUES ('BS HRM','BACHELOR OF SCIENCE IN HOTEL AND RESTAURANT MANAGEMENT');
INSERT INTO "coursedata" VALUES ('MA HISTORY','MASTER OF ARTS IN HISTORY');
INSERT INTO "coursedata" VALUES ('MS PHYSICS','MASTER OF SCIENCE IN PHYSICS');
INSERT INTO "coursedata" VALUES ('MS STAT','MASTER OF SCIENCE IN STATISTICS');
INSERT INTO "coursedata" VALUES ('MS MATH','MASTER OF ARTS IN MATHEMATICS');
INSERT INTO "coursedata" VALUES ('MS BIO','MASTER OF SCIENCE IN BIOLOGY');
INSERT INTO "coursedata" VALUES ('BS IS','BACHELOR OF SCIENCE IN INFORMATION SYSTEMS');
INSERT INTO "coursedata" VALUES ('MA FILIPINO','MASTER OF ARTS IN FILIPINO');
INSERT INTO "coursedata" VALUES ('MS CS','MASTER OF SCIENCE IN COMPUTER SCIENCE');
INSERT INTO "coursedata" VALUES ('BET-CHET','BACHELOR OF ENGINEERING TECHNOLOGY - CHEMICAL ENGINEERING TECHNOLOGY');
INSERT INTO "coursedata" VALUES ('BA PSYCH','BACHELOR OF ARTS IN PSYCHOLOGY');
INSERT INTO "coursedata" VALUES ('BA ELS','BACHELOR OF ARTS IN ENGLISH LANGUAGE STUDIES');
INSERT INTO "coursedata" VALUES ('BA PANITIKAN','BACHELOR OF ARTS IN PANITIKAN');
INSERT INTO "coursedata" VALUES ('BA SOCIO','BACHELOR OF ARTS IN SOCIOLOGY');
INSERT INTO "coursedata" VALUES ('MA ELS','MASTER OF ARTS IN ENGLISH LANGUAGE STUDIES');
INSERT INTO "coursedata" VALUES ('MA SOCIO','MASTER OF ARTS IN SOCIOLOGY');
INSERT INTO "coursedata" VALUES ('PHD FILIPINO','DOCTOR OF PHILOSOPHY IN FILIPINO');
INSERT INTO "coursedata" VALUES ('PHD LANGUAGE STUDIES','DOCTOR OF PHILOSOPHY IN LANGUAGE STUDIES');
INSERT INTO "coursedata" VALUES ('BSBA ECON','BACHELOR OF SCIENCE IN BUSINESS ADMINISTRATION - BUSINESS ECONOMICS');
INSERT INTO "coursedata" VALUES ('BS ECON','BACHELOR OF SCIENCE IN ECONOMICS');
INSERT INTO "coursedata" VALUES ('BS ENTRE','BACHELOR OF SCIENCE IN ENTREPRENEURSHIP');
INSERT INTO "coursedata" VALUES ('BS HM','BACHELOR OF SCIENCE IN HOSPITALITY MANAGEMENT');
INSERT INTO "coursedata" VALUES ('MS IT','MASTER OF SCIENCE IN INFORMATION TECHNOLOGY');
INSERT INTO "coursedata" VALUES ('MS INFO MANAGEMENT','MASTER OF SCIENCE IN INFORMATION MANAGEMENT');
INSERT INTO "coursedata" VALUES ('B PE','BACHELOR IN PHYSICAL EDUCATION');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-4981','Vequizo, Kiesha Pearl B.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-0565','Tercio, Jhon Ralfh Venecer H.','2nd Year','BS STAT','Male');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-1940','Telmoso, Jane Ann S.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-4906','Tala, Lynn Stefanny D.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-4733','Tagbo, Shilo V.','2nd Year','BS STAT','Male');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-4855','Revelo, Kathleen Claire U.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-3513','Randa, Eulyza R.','3rd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-2066','Rabago, Fel Andrei D.','2nd Year','BS STAT','Male');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-2292','Payusan, Justine B.','3rd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-4805','Pasco, Ranfil C.','2nd Year','BS STAT','Male');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-1453','Oledan, Christine Jane B.','3rd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-5442','Noval, Russel Gian C.','3rd Year','BS STAT','Male');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-2588','Musa, Widad P.','3rd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-2270','Martinez, Ryan James J.','3rd Year','BS STAT','Male');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-5181','Manos, Shiela Marie B.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-7504','Manigsaca, Grace Raquel E.','3rd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-4764','Mancera, Julibel  S.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-0212','Maisog, John Conrad Seg B.','3rd Year','BS STAT','Male');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-1508','Mainit, Dana B.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-3875','Madidis, Hannah Jane R.','3rd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-1952','Macalisang, Nifty Vaniah L.','3rd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-7736','Macalanggan, Cairoden U.','3rd Year','BS STAT','Male');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-1300','Lumayag, Judy Mae M.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-1193','Lucaser, Sheila Mae O.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-5636','Layawa, Charlene Mea A.','3rd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-1203','Lacubtan, Aj Jhones S.','3rd Year','BS STAT','Male');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-0085','Jalop, Karen D.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-4813','Inutan, Jezel Marie G.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-0997','Indino, Jolandex Mae O.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-6300','Hermosa, Jalen Rose V.','3rd Year','BS STAT','Male');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-1193','Hadjisalic, Raihana A.','3rd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-3432','Elga, Renalyn V.','3rd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-4732','Daluran, Dunevy D.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-2048','Cabiladas, Glynese Fritz D.','3rd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-0645','Bobadilla, Cyreene Joy P.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-3589','Bernardo, Aiko Marielle C.','3rd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-5307','Bentilacion, Mike Jerald B.','3rd Year','BS STAT','Male');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-0655','Bendit, Rutchegen C.','3rd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-4872','Bayal, Jerel Jane M.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-2351','Batocael, Margaret A.','3rd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-1828','Barlisan, Anna Rose M.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-1061','Bajao, Ma. Carmel N.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-8953','Bagul, Fatima L.','3rd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-4810','Badelles, Crizyl Mae C.','2nd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-8928','Asequia, Jahyah N.','3rd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-0021','Arcamo, Francis Ann Emmanuel G.','3rd Year','BS STAT','Male');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2019-3189','Apiag, Maica A.','3rd Year','BS STAT','Female');
INSERT INTO studentdata(stud_id,stud_name,stud_year,stud_course_id,stud_gender) VALUES ('2020-1813','Abaya, Mycah Therese T.','2nd Year','BS STAT','Female');
COMMIT;
