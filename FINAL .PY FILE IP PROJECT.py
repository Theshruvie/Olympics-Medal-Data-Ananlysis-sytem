#````LIBRARIES IMPORTED~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.transforms as ts
import pandas as pd
import mysql.connector as SQLAlchemy
import warnings
#~~~~~~~~~~~CONNECTING MYSQL TO PYTHON~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
con=SQLAlchemy.connect(host='localhost',user='root',passwd='shruvbae',database='olymp')
warnings.filterwarnings("ignore")
while con.is_connected():
    print("""
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::OLYMPICS MEDAL DATA ANALYSIS SYSTEM:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
1. SHOW ALL RECORDS
2. ADD RECORDS
3. SEARCH RECORDS
4. GRAPHICAL REPRESENTATION
5. DELETE RECORDS
6. UPDATE RECORDS
7. EXIT
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::""")
#FUNCTIONSS TO SHOW ALL THE RECORDS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    x=int(input('ENTER YOUR CHOICE:'))
    if x==1:
        print("""
==============================================
ALL TIME RECORDS OF TOP 10 COUNTRIES
==============================================
1. SUMMER OLYMPICS
2. WINTER OLYMPICS
3. COMBINED (SUMMER AND WINTER OLYMPICS)
4. BEIJING 2022 WINTER OLYMPICS
5. BACK TO MAIN MENU
==============================================""")
        ex=int(input('ENTER YOUR CHOICE: '))
        if ex==1:
            qry="select * from summer_olympics order by RANK_ asc";
            mdf=pd.read_sql(qry,con)
            print(mdf)
            print("""
================================
RETURNED TO MAIN MENU
================================""")
        if ex==2:
            qry2='select * from winter_olympics';
            mdf2=pd.read_sql(qry2,con)
            print(mdf2)
            print("""
================================
RETURNED TO MAIN MENU
================================""")
        if ex==3:
            qry3='select * from combined_total';
            mdf3=pd.read_sql(qry3,con)
            print(mdf3)
            print("""
================================
RETURNED TO MAIN MENU
================================""")
        if ex==4:
            qry4='select * from combined_total';
            mdf4=pd.read_sql(qry4,con)
            print(mdf4)
            print("""
================================
RETURNED TO MAIN MENU
================================""")
        if ex==5:
            print("""
==========================================
RETURNED TO MAIN MENU
=========================================""")
            print(x)
#FUNCTIONS TO ADD A RECORD~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~`            
    if x==2:
        print("""
======================================================
IN WHICH TABLE YOU'D LIKE TO ADD RECORD
======================================================
1. SUMMER OLYMPICS
2. WINTER OLYMPICS
3. COMBINED (SUMMER AND WINTER OLYMPICS)
4. BEIJING 2022 WINTER OLYMPICS
5. BACK TO MAIN MENU
=======================================================""")
        XR=int(input('ENTER YOUR CHOICE: '))
        if XR==1:
            print("""
======================================================
FORMAT
======================================================
1. ENTER RANK
2. ENTER NATION NAME
3. ENTER NO. OF GOLD MEDALS
4. ENTER NO. OF SILVER MEDALS
5. ENTER NO. OF BRONZE MEDALS
6. ENTER NO. OF TOTAL MEDALS(GOLD,SILVER,BRONZE)
======================================================""")
            RANK_=int(input('Enter rank:'))
            NATION_=input('Enter Nation:')
            GOLD_=int(input('Enter no. of gold medals: '))
            SILVER_=int(input('Enter number of Silver medals:'))
            BRONZE_=int(input('Enter number of bronze medals:'))
            TOTAL_=int(input('Enter total number of medals:'))
            quer="insert into summer_olympics values({},{},{},{},{},{});".format(RANK_,NATION_,GOLD_,SILVER_,BRONZE_,TOTAL_)
            cursor=con.cursor()
            cursor.execute(quer)
            con.commit()
            print("""ADDED SUCCESSFULLLY.....""")
            print("""
=====================================================================================
THE ADDED RECORD
======================================================================================
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
            cvvv=input("Enter added nation name: ")
            qry6='select * from summer_olympics where NATION_=%s;'%cvvv
            md6=pd.read_sql(qry6,con)
            print(md6)
            print("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
            
            print("""
================================
RETURNED TO MAIN MENU
================================""")

        if XR==2:
             print("""
======================================================
FORMAT
======================================================
1. ENTER RANK
2. ENTER NATION NAME
3. ENTER NO. OF GOLD MEDALS
4. ENTER NO. OF SILVER MEDALS
5. ENTER NO. OF BRONZE MEDALS
6. ENTER NO. OF TOTAL MEDALS(GOLD,SILVER,BRONZE)
======================================================""")
             RANK_=int(input('Enter rank:'))
             NATION_=input('Enter Nation:')
             GOLD_=int(input('Enter no. of gold medals: '))
             SILVER_=int(input('Enter number of Silver medals:'))
             BRONZE_=int(input('Enter number of bronze medals:'))
             TOTAL_=int(input('Enter total number of medals:'))
             quer="insert into winter_olympics values({},{},{},{},{},{});".format(RANK_,NATION_,GOLD_,SILVER_,BRONZE_,TOTAL_)
             cursor=con.cursor()
             cursor.execute(quer)
             con.commit()
             print("""ADDED SUCCESSFULLLY.....""")
             print("""
=====================================================================================
THE ADDED RECORD
======================================================================================
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
             
             cvvv=input("Enter added nation name: ")
             qry6='select * from winter_olympics where NATION_=%s;'%cvvv
             md6=pd.read_sql(qry6,con)
             print(md6)
             print("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
             print("""
================================
RETURNED TO MAIN MENU
================================""")

        if XR==3:
             print("""
======================================================
FORMAT
======================================================
1. ENTER RANK
2. ENTER NATION NAME
3. ENTER NO. OF GOLD MEDALS
4. ENTER NO. OF SILVER MEDALS
5. ENTER NO. OF BRONZE MEDALS
6. ENTER NO. OF TOTAL MEDALS(GOLD,SILVER,BRONZE)
======================================================""")
             RANK_=int(input('Enter rank:'))
             NATION_=input('Enter Nation:')
             GOLD_=int(input('Enter no. of gold medals: '))
             SILVER_=int(input('Enter number of Silver medals:'))
             BRONZE_=int(input('Enter number of bronze medals:'))
             TOTAL_=int(input('Enter total number of medals:'))
             quer="insert into combined_total values({},{},{},{},{},{});".format(RANK_,NATION_,GOLD_,SILVER_,BRONZE_,TOTAL_)
             cursor=con.cursor()
             cursor.execute(quer)
             con.commit()
             print("""ADDED SUCCESSFULLLY.....""")
             print("""
=====================================================================================
THE ADDED RECORD
======================================================================================
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
             cvvv=input("Enter added nation name: ")
             qry6='select * from combined_total where NATION_=%s;'%cvvv
             md6=pd.read_sql(qry6,con)
             print(md6)
             print("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
             print("""
================================
RETURNED TO MAIN MENU
================================""")
            
        if XR==4:
             print("""
======================================================
FORMAT
======================================================
1. ENTER RANK
2. ENTER NATION NAME
3. ENTER NO. OF GOLD MEDALS
4. ENTER NO. OF SILVER MEDALS
5. ENTER NO. OF BRONZE MEDALS
6. ENTER NO. OF TOTAL MEDALS(GOLD,SILVER,BRONZE)
======================================================""")
             RANK_=int(input('Enter rank:'))
             NATION_=input('Enter Nation:')
             GOLD_=int(input('Enter no. of gold medals:'))
             SILVER_=int(input('Enter number of Silver medals:'))
             BRONZE_=int(input('Enter number of bronze medals:'))
             TOTAL_=int(input('Enter total number of medals:'))
             quer="insert into beijing_2022_winterolympics values({},{},{},{},{},{});".format(RANK_,NATION_,GOLD_,SILVER_,BRONZE_,TOTAL_)
             cursor=con.cursor()
             cursor.execute(quer)
             con.commit()
             print("""ADDED SUCCESSFULLLY.....""")
             print("""
================================
RETURNED TO MAIN MENU
================================""")
             print("""
=====================================================================================
THE ADDED RECORD
======================================================================================
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
             cvvv=input("Enter added nation name: ")
             qry6='select * from beijing_2022_winterolympics where NATION_=%s;'%cvvv
             md6=pd.read_sql(qry6,con)
             print(md6)
             print("""
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++""")
             print("""
================================
RETURNED TO MAIN MENU
================================""")
             
             

             
         
#FUNCTIONS TO SEARCH A RECORD...............................................................
    
    if x==3:
       print("""
==============================================
which specific record you're searching for
==============================================
1. SUMMER OLYMPICS TABLE
2. WINTER OLYMPICS TABLE
3. COMBINED TOTAL
4. BEIJING 2022 WINTER OLYMPICS
5. BACK TO MAIN MENU
==============================================""")
       ep=int(input('ENTER YOUR CHOICE: '))
       if ep==1:
                 ke=int(input("Enter rank: "))
                 qry6='select * from summer_olympics where RANK_=%d;'%ke
                 md6=pd.read_sql(qry6,con)
                 print(md6)
                 print("""
================================
RETURNED TO MAIN MENU
================================""")
       if ep==2:
           ek=int(input("Enter rank: "))
           qry7='select * from winter_olympics where RANK_=%d;'%ek
           md7=pd.read_sql(qry7,con)
           print(md7)
           print("""
================================
RETURNED TO MAIN MENU
================================""")
       if ep==3:
           en=int(input("Enter rank: "))
           qry9='select * from combined_total where RANK_=%d;'%en
           md9=pd.read_sql(qry9,con)
           print(md9)
           print("""
================================
RETURNED TO MAIN MENU
================================""")
       if ep==4:
           ne=int(input("Enter rank: "))
           qry8='select * from beijing_2022_winterolympics where RANK_=%d;'%ne
           md8=pd.read_sql(qry8,con)
           print(md8)
           print("""
================================
RETURNED TO MAIN MENU
================================""")
       if ep==5:
           print("""
==================================================
RETURNED TO MAIN MENU
==================================================""")
           print(x)
#GRAPHICAL REPRESENTATIONS.........................................................
    if x==4:
         print("""
=========================================================
GRAPHICAL REPRESENTATIONS
=========================================================
1. LINEAR GRAPHS
2. BAR GRAPHS
3. HISTOGRAMS
4. BACK TO MAIN MENU
=========================================================""")
         kr=int(input('ENTER YOUR CHOICE: '))
#LINEAR GRAPHS         
         if kr==1:
              print("""
=====================================================
LINEAR GRAPHS
=====================================================
1. SUMMER OLYMPICS
2. WINTER OLYMPICS
3. COMBINED(WINTER AND SUMMER OLYMPICS
4. BEIJING 2022 WINTER OLYMPICS
5. BACK TO MAIN MENU
=====================================================""")
              ni=int(input("ENTER YOUR CHOICE: "))
              if ni==1:
                    md24='select * from summer_olympics';
                    df24=pd.read_sql(md24,con)
                    Countries=df24['NATION_']  
                    no_of_totalmedals=df24['TOTAL_']
                    no_of_goldmedals=df24['GOLD_']
                    no_of_silvermedals=df24['SILVER_']
                    no_of_bronzemedals=df24['BRONZE_']
                    plt.plot(Countries,no_of_totalmedals,linestyle=':',color='green',marker='.',label='TOTAL MEDALS')
                    plt.plot(Countries,no_of_goldmedals,linestyle='--',color='yellow',marker='.',label='GOLD MEDALS')
                    plt.plot(Countries,no_of_silvermedals,linestyle='--',color='silver',marker='.',label='SILVER MEDALS')
                    plt.plot(Countries,no_of_bronzemedals,linestyle='--',color='brown',marker='.',label='BRONZE MEDALS')
                    plt.legend()
                    xcry=np.arange(len(Countries))
                    plt.xticks(xcry,Countries,rotation=30)
                    plt.xlabel('Country~ ~ ~ >',fontsize=12,color='r')
                    plt.ylabel('No of Total Medals~~>',fontsize=12,color='r')
                    plt.title('MEDALS WON BY TOP 10 COUNTRIES\n',color='blue',fontsize=18)
                    plt.show()
                    
                    print("""
=======================================
RETUENED TO MAIN MENU
=======================================""")
                 
                    
              if ni==2:
                    md12='select * from winter_olympics';
                    df2=pd.read_sql(md12,con)
                    Countries=df2['NATION_']
                    no_of_goldmedals=df2['GOLD_']
                    no_of_silvermedals=df2['SILVER_']
                    no_of_bronzemedals=df2['BRONZE_']
                    no_of_totalmedals=df2['TOTAL_']
                    plt.plot(Countries,no_of_totalmedals,linestyle=':',color='green',marker='.',label='TOTAL MEDALS')
                    plt.plot(Countries,no_of_goldmedals,linestyle='--',color='yellow',marker='.',label='GOLD MEDALS')
                    plt.plot(Countries,no_of_silvermedals,linestyle='--',color='silver',marker='.',label='SILVER MEDALS')
                    plt.plot(Countries,no_of_bronzemedals,linestyle='--',color='brown',marker='.',label='BRONZE MEDALS')
                    plt.legend()
                    xi=np.arange(len(Countries))
                    plt.xticks(xi,Countries,rotation=30)
                    plt.xlabel('Country~ ~ ~ >',fontsize=12,color='r')
                    plt.ylabel('No of  Medals~~>',fontsize=12,color='r')
                    plt.title(' MEDALS WON BY TOP 10 COUNTRIES\n',color='blue',fontsize=18)
                    plt.show()
                
              if ni==3:
                    md16='select * from combined_total';
                    df16=pd.read_sql(md16,con)
                    Countries=df16['NATION_']
                    no_of_goldmedals=df16['GOLD_']
                    no_of_silvermedals=df16['SILVER_']
                    no_of_bronzemedals=df16['BRONZE_']
                    no_of_totalmedals=df16['TOTAL_']
                    plt.plot(Countries,no_of_totalmedals,linestyle=':',color='green',marker='.',label='TOTAL MEDALS')
                    plt.plot(Countries,no_of_goldmedals,linestyle='--',color='yellow',marker='.',label='GOLD MEDALS')
                    plt.plot(Countries,no_of_silvermedals,linestyle='--',color='silver',marker='.',label='SILVER MEDALS')
                    plt.plot(Countries,no_of_bronzemedals,linestyle='--',color='brown',marker='.',label='BRONZE MEDALS')
                    plt.legend()
                    xp=np.arange(len(Countries))
                    plt.xticks(xp,Countries,rotation=30)
                    plt.xlabel('Country~ ~ ~ >',fontsize=12,color='r')
                    plt.ylabel('No of Medals~~>',fontsize=12,color='r')
                    plt.title('MEDALS WON BY TOP 10 COUNTRIES\n',color='blue',fontsize=18)
                    plt.show()
              if ni==4:
                    md27='select * from beijing_2022_winterolympics';
                    df27=pd.read_sql(md27,con)
                    Countries=df27['NATION_']
                    no_of_goldmedals=df27['GOLD_']
                    no_of_silvermedals=df27['SILVER_']
                    no_of_bronzemedals=df27['BRONZE_']
                    no_of_totalmedals=df27['TOTAL_']
                    plt.plot(Countries,no_of_totalmedals,linestyle=':',color='green',marker='.',label='TOTAL MEDALS')
                    plt.plot(Countries,no_of_goldmedals,linestyle='--',color='yellow',marker='.',label='GOLD MEDALS')
                    plt.plot(Countries,no_of_silvermedals,linestyle='--',color='silver',marker='.',label='SILVER MEDALS')
                    plt.plot(Countries,no_of_bronzemedals,linestyle='--',color='brown',marker='.',label='BRONZE MEDALS')
                    plt.legend()
                    xx=np.arange(len(Countries))
                    plt.xticks(xx,Countries,rotation=30)
                    plt.xlabel('Country~ ~ ~ >',fontsize=12,color='r')
                    plt.ylabel('No of Medals~~>',fontsize=12,color='r')
                    plt.title('MEDALS WON BY TOP 10 COUNTRIES',color='blue',fontsize=18)
                    plt.show()
              if ni==5:
                 print(x)
#BAR GRAPHS             
         if kr==2:
            print("""
=============================================
BAR GRAPH
=============================================
1. SUMMMER OLYMPICS
2. WINTER OLYMPICS
3. COMBINED OLYMPICS
4. BEIJING 2022 WINTER OLYMPICs
5. BACK TO MAIN MENU
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~""")
            nep=int(input("ENTER YOUR CHOICE: "))
            if nep==1:
                md25='select * from summer_olympics';
                df25=pd.read_sql(md25,con)
                xsr=np.arange(len(df25))
                Countries=df25['NATION_']
                goldmedals=df25['GOLD_']
                silvermedals=df25 ['SILVER_']
                bronzemedals=df25 ['BRONZE_']
                totalmedals=df25['TOTAL_']
                plt.bar(xsr+0.0,goldmedals,label='Total No. of Gold Medals by Top 10 Countries IN SUMMER', width=0.2, color='yellow')
                plt.bar(xsr+0.2,silvermedals,label="Total No. of Silver Medals Top 10 Countries IN WINTER", width=0.2, color= 'grey')
                plt.bar(xsr+0.4,bronzemedals,label="Total No. of Bronze Medals Top 10 Countries IN WINTER", width=0.2, color= 'brown')
                plt.bar(xsr+0.6,totalmedals,label="Total No. of Medals Top 10 Countries IN WINTER", width=0.2, color= 'red')
                plt.xticks(xsr,Countries,rotation=20)
                plt.title('Summer Olympic Medal Analysis by Top 10 Countries',color='navy' ,fontsize= 16)
                plt.xlabel('Countries ~ ~ ~ ~ >',fontsize=12,color='r')
                plt.ylabel('No. of Medals~ ~ ~~ >',fontsize=12,color='r')
                plt.grid()
                plt.legend()
                plt.show()
                print("""
=========================================
RETURNED TO MAIN MENU
=========================================""")
            if nep==2:
                  md38='select * from winter_olympics';
                  df38=pd.read_sql(md38,con)
                  xsr=np.arange(len(df38))
                  Countries=df38['NATION_']
                  goldmedals=df38['GOLD_']
                  silvermedals=df38['SILVER_']
                  bronzemedals=df38 ['BRONZE_']
                  totalmedals=df38['TOTAL_']
                  plt.bar(xsr+0.0,goldmedals,label='Total No. of Gold Medals by Top 10 Countries IN SUMMER', width=0.2, color='yellow')
                  plt.bar(xsr+0.2,silvermedals,label="Total No. of Silver Medals Top 10 Countries IN WINTER", width=0.2, color= 'grey')
                  plt.bar(xsr+0.4,bronzemedals,label="Total No. of Bronze Medals Top 10 Countries IN WINTER", width=0.2, color= 'brown')
                  plt.bar(xsr+0.6,totalmedals,label="Total No. of Medals Top 10 Countries IN WINTER", width=0.2, color= 'red')
                  plt.xticks(xsr,Countries,rotation=20)
                  plt.title('Winter Olympic Medal Analysis by Top 10 Countries',color='navy' ,fontsize= 16)
                  plt.xlabel('Countries ~ ~ ~ ~ >',fontsize=12,color='r')
                  plt.ylabel('No. of Medals~ ~ ~~ >',fontsize=12,color='r')
                  plt.grid()
                  plt.legend()
                  plt.show()
                  print("""
=========================================
RETURNED TO MAIN MENU
=========================================""")
            if nep==3:
                mdk='select * from combined_total';
                dfk=pd.read_sql(mdk,con)
                xsr=np.arange(len(dfk))
                Countries=dfk['NATION_']
                goldmedals=dfk['GOLD_']
                silvermedals=dfk['SILVER_']
                bronzemedals=dfk['BRONZE_']
                totalmedals=dfk['TOTAL_']
                plt.bar(xsr+0.0,goldmedals,label='Total No. of Gold Medals by Top 10 Countries IN SUMMER', width=0.2, color='yellow')
                plt.bar(xsr+0.2,silvermedals,label="Total No. of Silver Medals Top 10 Countries IN WINTER", width=0.2, color= 'grey')
                plt.bar(xsr+0.4,bronzemedals,label="Total No. of Bronze Medals Top 10 Countries IN WINTER", width=0.2, color= 'brown')
                plt.bar(xsr+0.6,totalmedals,label="Total No. of Medals Top 10 Countries IN WINTER", width=0.2, color= 'red')
                plt.xticks(xsr,Countries,rotation=20)
                plt.title('Combined Olympics medal Analysis by Top 10 Countries',color='navy' ,fontsize= 16)
                plt.xlabel('Countries ~ ~ ~ ~ >',fontsize=12,color='r')
                plt.ylabel('No. of Medals~ ~ ~~ >',fontsize=12,color='r')
                plt.grid()
                plt.legend()
                plt.show()
                print("""
=========================================
RETURNED TO MAIN MENU
=========================================""")
            if nep==4:
                mdn='select * from beijing_2022_winterolympics';
                dfn=pd.read_sql(mdn,con)
                xsr=np.arange(len(dfn))
                Countries=dfn['NATION_']
                goldmedals=dfn['GOLD_']
                silvermedals=dfn['SILVER_']
                bronzemedals=dfn['BRONZE_']
                totalmedals=dfn['TOTAL_']
                plt.bar(xsr+0.0,goldmedals,label='Total No. of Gold Medals by Top 10 Countries IN SUMMER', width=0.2, color='yellow')
                plt.bar(xsr+0.2,silvermedals,label="Total No. of Silver Medals Top 10 Countries IN WINTER", width=0.2, color= 'grey')
                plt.bar(xsr+0.4,bronzemedals,label="Total No. of Bronze Medals Top 10 Countries IN WINTER", width=0.2, color= 'brown')
                plt.bar(xsr+0.6,totalmedals,label="Total No. of Medals Top 10 Countries IN WINTER", width=0.2, color= 'red')
                plt.xticks(xsr,Countries,rotation=20)
                plt.title('BEIJING 2022 WINTER OLYMPICS',color='navy' ,fontsize= 16)
                plt.xlabel('Countries ~ ~ ~ ~ >',fontsize=12,color='r')
                plt.ylabel('No. of Medals~ ~ ~~ >',fontsize=12,color='r')
                plt.grid()
                plt.legend()
                plt.show()
                print("""
=========================================
RETURNED TO MAIN MENU
=========================================""")
#HISTOGRAMS                 
         if kr==3:
             print("""
========================================
HISTOGRAMS
========================================
1. SUMMER OLYMPICS
2. WINTER OLYMPICS
3. COMBINED W AND S OLYMPICS
4. BEIJING 2022 WINTER OLYMPICS
========================================""")
             
             hen=int(input('ENTER YOUR CHOICE: '))
             if hen==1:
                 mdx='select * from summer_olympics';
                 dfx=pd.read_sql(mdx,con)
                 s=dfx['GOLD_']
                 g=dfx['SILVER_']
                 b=dfx['BRONZE_']
                 I=dfx['TOTAL_']
                 clm=['Bronze','Silver','Gold','Total']
                 plt.hist([b,s,g,I],rwidth=0.9,color=['gold','silver','brown','red'],label=clm)
                 plt.title(' Summer Olympic Medal Analysis',color='navy' ,fontsize= 16)
                 plt.xlabel('No. of Medals ~>',fontsize=12,color='b')
                 plt.ylabel('No. of Countries ~>',fontsize=12,color='b')
                 plt.grid() 
                 plt.legend()
                 plt.show()
                 print("""
=========================================
RETURNED TO MAIN MENU
=========================================""")
             if hen==2:
                 mdy='select * from winter_olympics';
                 dfy=pd.read_sql(mdy,con)
                 s=dfy['GOLD_']
                 g=dfy['SILVER_']
                 b=dfy['BRONZE_']
                 I=dfy['TOTAL_']
                 clm=['Bronze','Silver','Gold','Total']
                 plt.hist([b,s,g,I],rwidth=0.9,color=['gold','silver','brown','red'],label=clm)
                 plt.title(' Winter Olympic Medal Analysis',color='navy' ,fontsize= 16)
                 plt.xlabel('No. of Medals ~>',fontsize=12,color='b')
                 plt.ylabel('No. of Countries ~>',fontsize=12,color='b')
                 plt.grid() 
                 plt.legend()
                 plt.show()
                 print("""
=========================================
RETURNED TO MAIN MENU
=========================================""")
             if hen==3:
                 mdi='select * from combined_total';
                 dfi=pd.read_sql(mdi,con)
                 s=dfi['GOLD_']
                 g=dfi['SILVER_']
                 b=dfi['BRONZE_']
                 I=dfi['TOTAL_']
                 clm=['Bronze','Silver','Gold','Total']
                 plt.hist([b,s,g,I],rwidth=0.9,color=['gold','silver','brown','red'],label=clm)
                 plt.title(' Combined Olympics Medal Analysis',color='navy' ,fontsize= 16)
                 plt.xlabel('No. of Medals ~>',fontsize=12,color='b')
                 plt.ylabel('No. of Countries ~>',fontsize=12,color='b')
                 plt.grid() 
                 plt.legend()
                 plt.show()
                 print("""
=========================================
RETURNED TO MAIN MENU
=========================================""")
             if hen==4:
                 mdt='select * from beijing_2022_winterolympics';
                 dft=pd.read_sql(mdt,con)
                 s=dft['GOLD_']
                 g=dft['SILVER_']
                 b=dft['BRONZE_']
                 I=dft['TOTAL_']
                 clm=['Bronze','Silver','Gold','Total']
                 plt.hist([b,s,g,I],rwidth=0.9,color=['gold','silver','brown','red'],label=clm)
                 plt.title(' Beijjing 2022 winter olympics',color='navy' ,fontsize= 16)
                 plt.xlabel('No. of Medals ~>',fontsize=12,color='b')
                 plt.ylabel('No. of Countries ~>',fontsize=12,color='b')
                 plt.grid() 
                 plt.legend()
                 plt.show()
                 print("""
=========================================
RETURNED TO MAIN MENU
=========================================""")

             if kr==4:
              print(x)
#EXIT..............              
    if x==7:
        sys.exit()
#FUNCTIONS TO DELETE RECORDS        
    if x==5:
        print("""
========================================
1. SUMMER OLYMPICS
2. WINTER OLYMPICS
3. COMBINED OLYMPICS
4. BEIJING 2022 WINTER OLYMPICS
========================================""")
        krr=int(input('ENTER YOUR CHOICE: '))
        if krr==1:
            qry='select * from summer_olympics order by RANK_ asc;'
            mdf=pd.read_sql(qry,con)
            print(mdf)
            epp=(input('ENTER NATION:  '))
            quer="delete from summer_olympics where NATION_=%s;"%epp
            cursor=con.cursor()
            cursor.execute(quer)
            con.commit()
            print("DELETED SUCCESSFULLYYYY......")
            qry='select * from summer_olympics order by RANK_ asc;'
            mdf=pd.read_sql(qry,con)
            print(mdf)
            print("""
======================================
RETURNED TO MAIN MENU
======================================""")
            
        

        if krr==2:
            qry='select * from winter_olympics;'
            mdf=pd.read_sql(qry,con)
            print(mdf)
            epp=(input('ENTER NATION:  '))
            quer="delete from winter_olympics where NATION_=%s;"%epp
            cursor=con.cursor()
            cursor.execute(quer)
            con.commit()
            print("DELETED SUCCESSFULLYYYY......")
            qry='select * from winter_olympics;'
            mdf=pd.read_sql(qry,con)
            print(mdf)
            print("""
======================================
RETURNED TO MAIN MENU
======================================""")
        if krr==3:
            qry='select * from combined_total;'
            mdf=pd.read_sql(qry,con)
            print(mdf)
            epp=(input('ENTER NATION:  '))
            quer="delete from combined_total where NATION_=%s;"%epp
            cursor=con.cursor()
            cursor.execute(quer)
            con.commit()
            print("DELETED SUCCESSFULLYYYY......")
            qry='select * from combined_total;'
            mdf=pd.read_sql(qry,con)
            print(mdf)
            print("""
======================================
RETURNED TO MAIN MENU
z======================================""")
        if krr==4:
            qry='select * from beijing_2022_winterolympics;'
            mdf=pd.read_sql(qry,con)
            print(mdf)
            epp=(input('ENTER NATION:  '))
            quer="delete from beijing_2022_winterolympics where NATION_=%s;"%epp
            cursor=con.cursor()
            cursor.execute(quer)
            con.commit()
            print("DELETED SUCCESSFULLYYYY......")
            qry='select * from beijing_2022_winterolympics;'
            mdf=pd.read_sql(qry,con)
            print(mdf)
            print("""
======================================
RETURNED TO MAIN MENU
======================================""")
            

            
        
#FUNCTIONS TO UPDATE RECORDS        
        
        
    if x==6:
        print("""
=========================================
1. SUMMER OLYMPICS
2. WINTER OLYMPICS
3. COMBINED OLYMPICS
4. BEIJING 2022 WINTER OLYMPICS
5. BACK TO MAIN MENU
========================================""")
        sev=int(input('ENTER YOUR CHOICE: '))
        if sev==1:
            qry='select * from summer_olympics order by RANK_ asc;'
            mdf=pd.read_sql(qry,con)
            print(mdf)
            print('''
====================================
WHAT YOU'D LIKE TO UPDATE
++++++++++++++++++++++++++++++++++++
1. RANK
2. NATION
3. GOLD MEDALS
4. SILVER MEDALS
5. BRONZE MEDLAS
6. TOTAL MEDALS
7. WHOLE RECORD
=====================================''')
            krrr=int(input('ENTER YOUR CHOICE: '))
            if krrr==1:
                print('''
+++ENTER RANK YOU WANNA CHANGE+++''')
                upd1=int(input('Enter rank:'))
                print('''
+++ENTER NEW RANK+++''')
                upd2=int(input('ENTER NEW RANK:'))
                que='update summer_olympics set RANK_={} where RANK_={};'.format(upd2,upd1)
                cursor=con.cursor()
                cursor.execute(que)
                con.commit()
                print('''UPDATED SUCCESSFULLLYYY......''')
                qry='select * from summer_olympics order by RANK_ asc;'
                mdf=pd.read_sql(qry,con)
                print(mdf)
                print('''
========================
RETURNED TO MAIN MENU
========================''')
            if krrr==2:
                print('''
+++ENTER NATION NAME YOU WANNA CHANGE IN ('')+++''')
                upd1=input('Enter Nation:')
                print('''
+++ENTER NEW NATION NAME IN('')+++''')
                upd2=input('ENTER NATION NAME:')
                que='update summer_olympics set NATION_={} where NATION_={};'.format(upd2,upd1)
                cursor=con.cursor()
                cursor.execute(que)
                con.commit()
                print('''UPDATED SUCCESSFULLLYYY......''')
                qry='select * from summer_olympics order by RANK_ asc;'
                mdf=pd.read_sql(qry,con)
                print(mdf)
                print('''
========================
RETURNED TO MAIN MENU
========================''')
            if krrr==3:
                print('''
+++ENTER NO. OF GOLD MEDALS YOU WANNA CHANGE+++''')
                
                upd1=int(input('Enter no. of gold medals:'))
                print('''
+++ENTER UPDATED NO. OF GOLD MEDALS+++''')
                upd2=int(input('ENTER NO. OF GOLD MEDALS:'))
                que='update summer_olympics set GOLD_={} where GOLD_={};'.format(upd2,upd1)
                cursor=con.cursor()
                cursor.execute(que)
                con.commit()
                print('''UPDATED SUCCESSFULLLYYY......''')
                qry='select * from summer_olympics order by RANK_ asc;'
                mdf=pd.read_sql(qry,con)
                print(mdf)
                print('''
========================
RETURNED TO MAIN MENU
========================''')
            if krrr==4:
                print('''
+++ENTER NO. OF SILVER MEDALS YOU WANNA CHANGE+++''')
                upd1=int(input('ENTER NO. OF SILVER MEDALS:'))
                print('''
+++ENTER UPDATED NO. OF SILVER MEDALS+++''')
                upd2=int(input('ENTER NO. OF SILVER MEDALS:'))
                que='update summer_olympics set SILVER_={} where SILVER_={};'.format(upd2,upd1)
                cursor=con.cursor()
                cursor.execute(que)
                con.commit()
                print('''UPDATED SUCCESSFULLLYYY......''')
                qry='select * from summer_olympics order by RANK_ asc;'
                mdf=pd.read_sql(qry,con)
                print(mdf)
                print('''
========================
RETURNED TO MAIN MENU
========================''')
            if krrr==5:
                 print('''
+++ENTER NO. OF BRONZE MEDALS YOU WANNA CHANGE+++''')
                 upd1=int(input('ENTER NO. OF BRONZE MEDALS:'))
                 print('''
+++ENTER UPDATED NO. OF BRONZE MEDALS+++''')
                 upd2=int(input('ENTER NO. OF BRONZE MEDALS:'))
                 que='update summer_olympics set BRONZE_={} where BRONZE_={};'.format(upd2,upd1)
                 cursor=con.cursor()
                 cursor.execute(que)
                 con.commit()
                 print('''UPDATED SUCCESSFULLLYYY......''')
                 qry='select * from summer_olympics order by RANK_ asc;'
                 mdf=pd.read_sql(qry,con)
                 print(mdf)
                 print('''
========================
RETURNED TO MAIN MENU
========================''')
            if krrr==6:
                 print('''
+++ENTER TOTAL NO. OF MEDALS YOU WANNA CHANGE+++''')
                 upd1=int(input('ENTER TOTAL NO. OF MEDALS:'))
                 print('''
+++ENTER UPDATED NO. OF SILVER MEDALS+++''')
                 upd2=int(input('ENTER TOTAL NO. OF MEDALS:'))
                 que='update summer_olympics set TOTAL_={} where TOTAL_={};'.format(upd2,upd1)
                 cursor=con.cursor()
                 cursor.execute(que)
                 con.commit()
                 print('''UPDATED SUCCESSFULLLYYY......''')
                 qry='select * from winter_olympics order by RANK_ asc;'
                 mdf=pd.read_sql(qry,con)
                 print(mdf)
                 print('''
========================
RETURNED TO MAIN MENU
========================''')
            if krrr==7:
                crin=int(input('Enter rank:'))
                quer="delete from winter_olympics where RANK_={}".format(crin)
                cursor=con.cursor()
                cursor.execute(quer)
                con.commit()
                print("""
=================================
ENTER YOUR UPDATED DATA
=================================""")
                RANK_=int(input('Enter rank:'))
                NATION_=input('Enter Nation;')
                GOLD_=int(input('Enter no. of gold medals; '))
                SILVER_=int(input('Enter number of Silver medals:'))
                BRONZE_=int(input('Enter number of bronze medals:'))
                TOTAL_=int(input('Enter total number of medals:'))
                quer="insert into winter_olympics values({},{},{},{},{},{});".format(RANK_,NATION_,GOLD_,SILVER_,BRONZE_,TOTAL_)
                cursor=con.cursor()
                cursor.execute(quer)
                con.commit()
                print("""
=======================================
DATA UPDATED SUCCESSFULLY
======================================
++++++++++++++++++++++++++++++++++++++""")
                qry='select * from winter_olympics order by RANK_ asc;'
                mdf=pd.read_sql(qry,con)
                print(mdf)
                print("""
++++++++++++++++++++++++++++++++++++++
======================================
RETURNED TO MAIN MENU
=======================================""")
        if sev==2:
            qry='select * from winter_olympics;'
            mdf=pd.read_sql(qry,con)
            print(mdf)
            print('''
====================================
WHAT YOU'D LIKE TO UPDATE
++++++++++++++++++++++++++++++++++++
1. RANK
2. NATION
3. GOLD MEDALS
4. SILVER MEDALS
5. BRONZE MEDLAS
6. TOTAL MEDALS
7. WHOLE RECORD
=====================================''')
            ksrr=int(input('ENTER YOUR CHOICE: '))
            if ksrr==1:
                print('''
+++ENTER RANK YOU WANNA CHANGE+++''')
                upd1=int(input('Enter rank:'))
                print('''
+++ENTER NEW RANK+++''')
                upd2=int(input('ENTER NEW RANK:'))
                que='update winter_olympics set RANK_={} where RANK_={};'.format(upd2,upd1)
                cursor=con.cursor()
                cursor.execute(que)
                con.commit()
                print('''UPDATED SUCCESSFULLLYYY......''')
                qry='select * from winter_olympics;'
                mdf=pd.read_sql(qry,con)
                print(mdf)
                print('''
========================
RETURNED TO MAIN MENU
========================''')
            if ksrr==2:
                print('''
+++ENTER NATION NAME YOU WANNA CHANGE IN ('')+++''')
                upd1=input('Enter Nation:')
                print('''
+++ENTER NEW NATION NAME IN('')+++''')
                upd2=input('ENTER NATION NAME:')
                que='update winter_olympics set NATION_={} where NATION_={};'.format(upd2,upd1)
                cursor=con.cursor()
                cursor.execute(que)
                con.commit()
                print('''UPDATED SUCCESSFULLLYYY......''')
                qry='select * from winter_olympics;'
                mdf=pd.read_sql(qry,con)
                print(mdf)
                print('''
========================
RETURNED TO MAIN MENU
========================''')
            if ksrr==3:
                print('''
+++ENTER NO. OF GOLD MEDALS YOU WANNA CHANGE+++''')
                upd1=int(input('Enter no. of gold medals:'))
                print('''
+++ENTER UPDATED NO. OF GOLD MEDALS+++''')
                upd2=int(input('ENTER NO. OF GOLD MEDALS:'))
                que='update winter_olympics set GOLD_={} where GOLD_={};'.format(upd2,upd1)
                cursor=con.cursor()
                cursor.execute(que)
                con.commit()
                print('''UPDATED SUCCESSFULLLYYY......''')
                qry='select * from winter_olympics;'
                mdf=pd.read_sql(qry,con)
                print(mdf)
                print('''
=======================
RETURNED TO MAIN MENU
========================''')
            if ksrr==4:
                print('''
+++ENTER NO. OF SILVER MEDALS YOU WANNA CHANGE+++''')
                upd1=int(input('ENTER NO. OF SILVER MEDALS:'))
                print('''
+++ENTER UPDATENO. OF SILVER MEDALS+++''')
                upd2=int(input('ENTER NO. OF SILVER MEDALS:'))
                que='update winter_olympics set SILVER_={} where SILVER_={};'.format(upd2,upd1)
                cursor=con.cursor()
                cursor.execute(que)
                con.commit()
                print('''UPDATED SUCCESSFULLLYYY......''')
                qry='select * from winter_olympics;'
                mdf=pd.read_sql(qry,con)
                print(mdf)
                print('''
========================
RETURNED TO MAIN MENU
========================''')
            if ksrr==5:
                 print('''
+++ENTER NO. OF BRONZE MEDALS YOU WANNA CHANGE+++''')
                 upd1=int(input('ENTER NO. OF BRONZE MEDALS:'))
                 print('''
+++ENTER UPDATED NO. OF BRONZE MEDALS+++''')
                 upd2=int(input('ENTER NO. OF BRONZE MEDALS:'))
                 que='update winter_olympics set BRONZE_={} where BRONZE_={};'.format(upd2,upd1)
                 cursor=con.cursor()
                 cursor.execute(que)
                 con.commit()
                 print('''UPDATED SUCCESSFULLLYYY......''')
                 qry='select * from winter_olympics;'
                 mdf=pd.read_sql(qry,con)
                 print(mdf)
                 print('''
========================
RETURNED TO MAIN MENU
========================''')
            if ksrr==6:
                 print('''
+++ENTER TOTAL NO. OF MEDALS YOU WANNA CHANGE+++''')
                 upd1=int(input('ENTER TOTAL NO. OF MEDALS:'))
                 print('''
+++ENTER UPDATED NO. OF SILVER MEDALS+++''')
                 upd2=int(input('ENTER TOTAL NO. OF MEDALS:'))
                 que='update winter_olympics set TOTAL_={} where TOTAL_={};'.format(upd2,upd1)
                 cursor=con.cursor()
                 cursor.execute(que)
                 con.commit()
                 print('''UPDATED SUCCESSFULLLYYY......''')
                 qry='select * from winter_olympics;'
                 mdf=pd.read_sql(qry,con)
                 print(mdf)
                 print('''
========================
RETURNED TO MAIN MENU
========================''')
            if ksrr==7:
                err='select * from winter_olympics;'
                mdf=pd.read_sql(err,con)
                print(mdf)
                csea=int(input('Enter Rank:'))
                queryy="delete from winter_olympics where RANK_={}"%csea
                cursor=con.cursor()
                cursor.execute(queryy)
                con.commit()
                print("""
=================================
ENTER YOUR UPDATED DATA
=================================""")
                RANK_=int(input('Enter rank:'))
                NATION_=input('Enter Nation;')
                GOLD_=int(input('Enter no. of gold medals; '))
                SILVER_=int(input('Enter number of Silver medals:'))
                BRONZE_=int(input('Enter number of bronze medals:'))
                TOTAL_=int(input('Enter total number of medals:'))
                query="insert into winter_olympics values({},{},{},{},{},{});".format(RANK_,NATION_,GOLD_,SILVER_,BRONZE_,TOTAL_)
                cursor=con.cursor()
                cursor.execute(query)
                con.commit()
                err='select * from winter_olympics;'
                mdf=pd.read_sql(err,con)
                print(mdf)
                print("""
=======================================
DATA UPDATED SUCCESSFULLY
======================================
++++++++++++++++++++++++++++++++++++++
======================================
RETURNED TO MAIN MENU
=======================================""")
            
            
        if sev==3:
            qry='select * from combined_total;'
            mdf=pd.read_sql(qry,con)
            print(mdf)
            print('''
====================================
WHAT YOU'D LIKE TO UPDATE
++++++++++++++++++++++++++++++++++++
1. RANK
2. NATION
3. GOLD MEDALS
4. SILVER MEDALS
5. BRONZE MEDLAS
6. TOTAL MEDALS
7. WHOLE RECORD
=====================================''')
            kssr=int(input('ENTER YOUR CHOICE: '))
            if kssr==1:
                print('''
+++ENTER RANK YOU WANNA CHANGE+++''')
                upd1=int(input('Enter rank:'))
                print('''
+++ENTER NEW RANK+++''')
                upd2=int(input('ENTER NEW RANK:'))
                que='update combined_total set RANK_={} where RANK_={};'.format(upd2,upd1)
                cursor=con.cursor()
                cursor.execute(que)
                con.commit()
                print('''UPDATED SUCCESSFULLLYYY......''')
                qry='select * from combined_total;'
                mdf=pd.read_sql(qry,con)
                print(mdf)
                print('''
========================
RETURNED TO MAIN MENU
========================''')
            if kssr==2:
                print('''
+++ENTER NATION NAME YOU WANNA CHANGE IN ('')+++''')
                upd1=input('Enter Nation:')
                print('''
+++ENTER NEW NATION NAME IN('')+++''')
                upd2=input('ENTER NATION NAME:')
                que='update combined_total set NATION_={} where NATION_={};'.format(upd2,upd1)
                cursor=con.cursor()
                cursor.execute(que)
                con.commit()
                print('''UPDATED SUCCESSFULLLYYY......''')
                qry='select * from combined_total;'
                mdf=pd.read_sql(qry,con)
                print(mdf)
                print('''
========================
RETURNED TO MAIN MENU
========================''')
            if kssr==3:
                print('''
+++ENTER NO. OF GOLD MEDALS YOU WANNA CHANGE+++''')
                upd1=int(input('Enter no. of gold medals:'))
                print('''
+++ENTER UPDATED NO. OF GOLD MEDALS+++''')
                upd2=int(input('ENTER NO. OF GOLD MEDALS:'))
                que='update combined_total set GOLD_={} where GOLD_={};'.format(upd2,upd1)
                cursor=con.cursor()
                cursor.execute(que)
                con.commit()
                print('''UPDATED SUCCESSFULLLYYY......''')
                qry='select * from combined_total;'
                mdf=pd.read_sql(qry,con)
                print(mdf)
                print('''
========================
RETURNED TO MAIN MENU
========================''')
            if kssr==4:
                print('''
+++ENTER NO. OF SILVER MEDALS YOU WANNA CHANGE+++''')
                upd1=int(input('ENTER NO. OF SILVER MEDALS:'))
                print('''
+++ENTER UPDATED NO. OF SILVER MEDALS+++''')
                upd2=int(input('ENTER NO. OF SILVER MEDALS:'))
                que='update combined_total set SILVER_={} where SILVER_={};'.format(upd2,upd1)
                cursor=con.cursor()
                cursor.execute(que)
                con.commit()
                print('''UPDATED SUCCESSFULLLYYY......''')
                qry='select * from combined_total;'
                mdf=pd.read_sql(qry,con)
                print(mdf)
                print('''
========================
RETURNED TO MAIN MENU
========================''')
            if kssr==5:
                 print('''
+++ENTER NO. OF BRONZE MEDALS YOU WANNA CHANGE+++''')
                 upd1=int(input('ENTER NO. OF BRONZE MEDALS:'))
                 print('''
+++ENTER UPDATED NO. OF BRONZE MEDALS+++''')
                 upd2=int(input('ENTER NO. OF BRONZE MEDALS:'))
                 que='update combined_total set BRONZE_={} where BRONZE_={};'.format(upd2,upd1)
                 cursor=con.cursor()
                 cursor.execute(que)
                 con.commit()
                 print('''UPDATED SUCCESSFULLLYYY......''')
                 qry='select * from combined_total;'
                 mdf=pd.read_sql(qry,con)
                 print(mdf)
                 print('''
========================
RETURNED TO MAIN MENU
========================''')
            if kssr==6:
                 print('''
+++ENTER TOTAL NO. OF MEDALS YOU WANNA CHANGE+++''')
                 upd1=int(input('ENTER TOTAL NO. OF MEDALS:'))
                 print('''
+++ENTER UPDATED NO. OF SILVER MEDALS+++''')
                 upd2=int(input('ENTER TOTAL NO. OF MEDALS:'))
                 que='update combined_total set TOTAL_={} where TOTAL_={};'.format(upd2,upd1)
                 cursor=con.cursor()
                 cursor.execute(que)
                 con.commit()
                 print('''UPDATED SUCCESSFULLLYYY......''')
                 qry='select * from combined_total;'
                 mdf=pd.read_sql(qry,con)
                 print(mdf)
                 print('''
========================
RETURNED TO MAIN MENU
========================''')
            if kssr==7:
            
             crea=int(input('Enter Rank:'))
             quer="delete from combined_total where RANK_={}"%crea
             cursor=con.cursor()
             cursor.execute(quer)
             con.commit()
             print("""
=================================
ENTER YOUR UPDATED DATA
=================================""")
             RANK_=int(input('Enter rank:'))
             NATION_=input('Enter Nation;')
             GOLD_=int(input('Enter no. of gold medals; '))
             SILVER_=int(input('Enter number of Silver medals:'))
             BRONZE_=int(input('Enter number of bronze medals:'))
             TOTAL_=int(input('Enter total number of medals:'))
             query="insert into combined_total values({},{},{},{},{},{});".format(RANK_,NATION_,GOLD_,SILVER_,BRONZE_,TOTAL_)
             cursor=con.cursor()
             cursor.execute(query)
             con.commit()
             print("""
=======================================
DATA UPDATED SUCCESSFULLY
======================================
++++++++++++++++++++++++++++++++++++++
======================================
RETURNED TO MAIN MENU
=======================================""")
        if sev==4:
            qry='select * from beijing_2022_winterolympics;'
            mdf=pd.read_sql(qry,con)
            print(mdf)
            print('''
====================================
WHAT YOU'D LIKE TO UPDATE
++++++++++++++++++++++++++++++++++++
1. RANK
2. NATION
3. GOLD MEDALS
4. SILVER MEDALS
5. BRONZE MEDLAS
6. TOTAL MEDALS
7. WHOLE RECORD
=====================================''')
            ksss=int(input('ENTER YOUR CHOICE: '))
            if ksss==1:
                print('''
+++ENTER RANK YOU WANNA CHANGE+++''')
                upd1=int(input('Enter rank:'))
                print('''
+++ENTER NEW RANK+++''')
                upd2=int(input('ENTER NEW RANK:'))
                que='update beijing_2022_winterolympics set RANK_={} where RANK_={};'.format(upd2,upd1)
                cursor=con.cursor()
                cursor.execute(que)
                con.commit()
                print('''UPDATED SUCCESSFULLLYYY......''')
                qry='select * from beijing_2022_winterolympics;'
                mdf=pd.read_sql(qry,con)
                print(mdf)
                print('''
========================
RETURNED TO MAIN MENU
========================''')
            if ksss==2:
                print('''
+++ENTER NATION NAME YOU WANNA CHANGE IN ('')+++''')
                upd1=input('Enter Nation:')
                print('''
+++ENTER NEW NATION NAME IN('')+++''')
                upd2=input('ENTER NATION NAME:')
                que='update beijing_2022_winterolympics set NATION_={} where NATION_={};'.format(upd2,upd1)
                cursor=con.cursor()
                cursor.execute(que)
                con.commit()
                print('''UPDATED SUCCESSFULLLYYY......''')
                qry='select * from beijing_2022_winterolympics;'
                mdf=pd.read_sql(qry,con)
                print(mdf)
                print('''
========================
RETURNED TO MAIN MENU
========================''')
            if ksss==3:
                print('''
+++ENTER NO. OF GOLD MEDALS YOU WANNA CHANGE+++''')
                upd1=int(input('Enter no. of gold medals:'))
                print('''
+++ENTER UPDATED NO. OF GOLD MEDALS+++''')
                upd2=int(input('ENTER NO. OF GOLD MEDALS:'))
                que='update beijing_2022_winterolympics set GOLD_={} where GOLD_={};'.format(upd2,upd1)
                cursor=con.cursor()
                cursor.execute(que)
                con.commit()
                print('''UPDATED SUCCESSFULLLYYY......''')
                qry='select * from beijing_2022_winterolympics;'
                mdf=pd.read_sql(qry,con)
                print(mdf)
                print('''
========================
RETURNED TO MAIN MENU
========================''')
            if ksss==4:
                print('''
+++ENTER NO. OF SILVER MEDALS YOU WANNA CHANGE+++''')
                upd1=int(input('ENTER NO. OF SILVER MEDALS:'))
                print('''
+++ENTER UPDTED NO. OF SILVER MEDALS+++''')
                upd2=int(input('ENTER NO. OF SILVER MEDALS:'))
                que='update beijing_2022_winterolympics set SILVER_={} where SILVER_={};'.format(upd2,upd1)
                cursor=con.cursor()
                cursor.execute(que)
                con.commit()
                print('''UPDATED SUCCESSFULLLYYY......''')
                qry='select * from beijing_2022_winterolympics;'
                mdf=pd.read_sql(qry,con)
                print(mdf)
                print('''
========================
RETURNED TO MAIN MENU
========================''')
            if ksss==5:
                 print('''
+++ENTER NO. OF BRONZE MEDALS YOU WANNA CHANGE+++''')
                 upd1=int(input('ENTER NO. OF BRONZE MEDALS:'))
                 print('''
+++ENTER UPDATED NO. OF BRONZE MEDALS+++''')
                 upd2=int(input('ENTER NO. OF BRONZE MEDALS:'))
                 que='update beijing_2022_winterolympics set BRONZE_={} where BRONZE_={};'.format(upd2,upd1)
                 cursor=con.cursor()
                 cursor.execute(que)
                 con.commit()
                 print('''UPDATED SUCCESSFULLLYYY......''')
                 qry='select * from beijing_2022_winterolympics;'
                 mdf=pd.read_sql(qry,con)
                 print(mdf)
                 print('''
========================
RETURNED TO MAIN MENU
========================''')
            if ksss==6:
                 print('''
+++ENTER TOTAL NO. OF MEDALS YOU WANNA CHANGE+++''')
                 upd1=int(input('ENTER TOTAL NO. OF MEDALS:'))
                 print('''
+++ENTER UPDATED NO. OF SILVER MEDALS+++''')
                 upd2=int(input('ENTER TOTAL NO. OF MEDALS:'))
                 que='update beijing_2022_winterolympics set TOTAL_={} where TOTAL_={};'.format(upd2,upd1)
                 cursor=con.cursor()
                 cursor.execute(que)
                 con.commit()
                 print('''UPDATED SUCCESSFULLLYYY......''')
                 qry='select * from beijing_2022_winterolympics;'
                 mdf=pd.read_sql(qry,con)
                 print(mdf)
                 print('''
========================
RETURNED TO MAIN MENU
========================''')
            if ksss==7:
            
             crea=int(input('Enter Rank:'))
             quer="delete from beijing_2022_winterolympics where RANK_={}"%crea
             cursor=con.cursor()
             cursor.execute(quer)
             con.commit()
             print("""
=================================
ENTER YOUR UPDATED DATA
=================================""")
             RANK_=int(input('Enter rank:'))
             NATION_=input('Enter Nation;')
             GOLD_=int(input('Enter no. of gold medals; '))
             SILVER_=int(input('Enter number of Silver medals:'))
             BRONZE_=int(input('Enter number of bronze medals:'))
             TOTAL_=int(input('Enter total number of medals:'))
             query="insert into beijing_2022_winterolympics ({},{},{},{},{},{});".format(RANK_,NATION_,GOLD_,SILVER_,BRONZE_,TOTAL_)
             cursor=con.cursor()
             cursor.execute(query)
             con.commit()
             qry='select * from beijing_2022_winterolympics;'
             mdf=pd.read_sql(qry,con)
             print(mdf)
             print("""
=======================================
DATA UPDATED SUCCESSFULLY
======================================
++++++++++++++++++++++++++++++++++++++
======================================
RETURNED TO MAIN MENU
=======================================""")
        
        
              
              
              
                 
                 
                
                 
            
                 
