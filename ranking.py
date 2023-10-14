# Step 1: Connect to MongoDB and retrieve the data
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/ResBac")
db = client["ResBac"]
collection = db["BAC_2023"]
students_data = collection.find({})

#==================RANKING BY SERIE=====================

serie = collection.distinct("SERIE")
print(serie)
wilaya = collection.distinct("WILAYA_FR")

V = collection.find({"NODOSS": 23700})

# dec = collection.distinct("Decision")
# print(dec)
    
# for bacc_type in serie:
#     # Step 1: Retrieve the data from the MongoDB collection for the specific baccalaureate type
#     students_data = collection.find({"SERIE": bacc_type})

#     # Step 2: Filter successful students based on grade criteria and decision
#     successful_students = [
#         student for student in students_data
#         if (student["Decision"] in ['Admis ', 'Sessionnaire'] and student["SERIE"] == bacc_type)
#     ]
#     for wilaya_name in wilaya:
#         students_wilaya = collection.find({"WILAYA_FR": wilaya_name})

#         successful_wilaya = [
#             student for student in students_wilaya
#             if (student["Decision"] in ['Admis ', 'Sessionnaire'] and student["WILAYA_FR"] == wilaya_name and student['SERIE'] == bacc_type)
#         ]

#         successful_wilaya.sort(key=lambda x: x["MOYBAC"], reverse=True)

#         for rank, student in enumerate(successful_wilaya, start=1):
#             collection.update_one({"_id": student["_id"]}, {"$set": {"rank_Wilaya": rank}})

#     # Step 3: Sort successful students by rounded_moy in descending order to get the ranking
#     successful_students.sort(key=lambda x: x["MOYBAC"], reverse=True)

#     # Step 4: Update the documents with the respective rankings
#     for rank, student in enumerate(successful_students, start=1):
#         collection.update_one({"_id": student["_id"]}, {"$set": {"rank_N": rank}})

#=================FIN RANKING BY SERIE====================

#================RANKING BY WILAYA========================================================================




    
#================FIN RANKING BY WILAYA====================================================================



# collection.update_many(
#     {},
#     [
#         {
#             "$set": {
#                 "rounded_moy": {"$round": ["$MOYBAC", 2]}
#             }
#         }
#     ]
# )

# Update all documents in the collection to remove the "rank_n" field
# collection.update_many({}, {"$unset": {"rank_N": ""}})

# collection.update_many(
#     {"Decision": "Delibérable"},
#     {"$set": {"Decision": "Admis " , "rounded_moy": 10}}
# )