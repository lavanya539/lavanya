#!/usr/bin/env python3
"""
FractionEHR — Download all site images
Run this script on your computer: python3 download_all.py
Then upload the "fractionehr-assets" folder to GitHub.
"""
import urllib.request, os, time, sys

images = [
  {
    "url": "https://www.figma.com/api/mcp/asset/c0d28a79-e143-4039-95a6-14df6061302c",
    "filename": "fractionehr-assets/home/c0d28a79.jpg",
    "page": "home",
    "uid": "c0d28a79-e143-4039-95a6-14df6061302c"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/36b15c9b-ddcf-4070-b999-1c965a7c735c",
    "filename": "fractionehr-assets/home/36b15c9b.jpg",
    "page": "home",
    "uid": "36b15c9b-ddcf-4070-b999-1c965a7c735c"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/115e9ed9-aa08-470f-9796-c8764a90582f.png",
    "filename": "fractionehr-assets/home/115e9ed9.png",
    "page": "home",
    "uid": "115e9ed9-aa08-470f-9796-c8764a90582f.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/5d98cd5a-6df7-4c95-bb39-ab1f8512dd29",
    "filename": "fractionehr-assets/home/5d98cd5a.jpg",
    "page": "home",
    "uid": "5d98cd5a-6df7-4c95-bb39-ab1f8512dd29"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/6e1abacb-1e63-44f9-9467-eca80c22379b",
    "filename": "fractionehr-assets/home/6e1abacb.jpg",
    "page": "home",
    "uid": "6e1abacb-1e63-44f9-9467-eca80c22379b"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/2fd05983-8c70-4fa9-9830-a298e937f36b",
    "filename": "fractionehr-assets/home/2fd05983.jpg",
    "page": "home",
    "uid": "2fd05983-8c70-4fa9-9830-a298e937f36b"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/c1889526-567d-4db6-bbc7-9b6330d409d5",
    "filename": "fractionehr-assets/home/c1889526.jpg",
    "page": "home",
    "uid": "c1889526-567d-4db6-bbc7-9b6330d409d5"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/b8321dfa-73ab-4bc4-8614-6dda0c8a23ea",
    "filename": "fractionehr-assets/home/b8321dfa.jpg",
    "page": "home",
    "uid": "b8321dfa-73ab-4bc4-8614-6dda0c8a23ea"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/7bebea69-ba2d-4477-9941-6a135df26bde",
    "filename": "fractionehr-assets/home/7bebea69.jpg",
    "page": "home",
    "uid": "7bebea69-ba2d-4477-9941-6a135df26bde"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/b1ca8232-68f0-4ede-b42a-0b754b6ef321",
    "filename": "fractionehr-assets/home/b1ca8232.jpg",
    "page": "home",
    "uid": "b1ca8232-68f0-4ede-b42a-0b754b6ef321"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/8f3f951e-b4d1-4873-96ee-d3faf4def68a",
    "filename": "fractionehr-assets/home/8f3f951e.jpg",
    "page": "home",
    "uid": "8f3f951e-b4d1-4873-96ee-d3faf4def68a"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/38722efc-ca65-4f19-8c92-edbdea940d91",
    "filename": "fractionehr-assets/home/38722efc.jpg",
    "page": "home",
    "uid": "38722efc-ca65-4f19-8c92-edbdea940d91"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/751c8d15-127e-45c3-8d58-25996acd1ec4",
    "filename": "fractionehr-assets/home/751c8d15.jpg",
    "page": "home",
    "uid": "751c8d15-127e-45c3-8d58-25996acd1ec4"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/f5b8f58d-ff26-41dd-9353-ee4a0375904b",
    "filename": "fractionehr-assets/home/f5b8f58d.jpg",
    "page": "home",
    "uid": "f5b8f58d-ff26-41dd-9353-ee4a0375904b"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/b7944520-d6fb-4244-81a8-54a07657038c",
    "filename": "fractionehr-assets/home/b7944520.jpg",
    "page": "home",
    "uid": "b7944520-d6fb-4244-81a8-54a07657038c"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/27f14961-ed02-4af5-a3c5-05a33adbf22e",
    "filename": "fractionehr-assets/home/27f14961.jpg",
    "page": "home",
    "uid": "27f14961-ed02-4af5-a3c5-05a33adbf22e"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/608b21b2-f923-4cbb-82c8-a6ed20993a7e",
    "filename": "fractionehr-assets/home/608b21b2.jpg",
    "page": "home",
    "uid": "608b21b2-f923-4cbb-82c8-a6ed20993a7e"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/72989b5b-9f22-4030-b432-8b63399966c1",
    "filename": "fractionehr-assets/home/72989b5b.jpg",
    "page": "home",
    "uid": "72989b5b-9f22-4030-b432-8b63399966c1"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/286828fe-034d-4455-abc4-7c5afe0fdd2b.png",
    "filename": "fractionehr-assets/home/286828fe.png",
    "page": "home",
    "uid": "286828fe-034d-4455-abc4-7c5afe0fdd2b.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/ac61f9c2-2b72-4809-897b-f45ccf4cdcd1.png",
    "filename": "fractionehr-assets/patient-records/ac61f9c2.png",
    "page": "patient-records",
    "uid": "ac61f9c2-2b72-4809-897b-f45ccf4cdcd1.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/5c87baeb-0e5e-485e-804b-390d0e72538e.png",
    "filename": "fractionehr-assets/patient-records/5c87baeb.png",
    "page": "patient-records",
    "uid": "5c87baeb-0e5e-485e-804b-390d0e72538e.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/f59b2dfb-b4be-49b9-b00a-585f10adb307.png",
    "filename": "fractionehr-assets/patient-records/f59b2dfb.png",
    "page": "patient-records",
    "uid": "f59b2dfb-b4be-49b9-b00a-585f10adb307.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/01f1717a-a16d-4a6b-9668-68301356ba90.png",
    "filename": "fractionehr-assets/digital-intake/01f1717a.png",
    "page": "digital-intake",
    "uid": "01f1717a-a16d-4a6b-9668-68301356ba90.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/585188c0-cce6-464c-bfb6-d5084e024705.png",
    "filename": "fractionehr-assets/digital-intake/585188c0.png",
    "page": "digital-intake",
    "uid": "585188c0-cce6-464c-bfb6-d5084e024705.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/4d6fe2cd-201e-45b6-8677-3a2ee72f4174.png",
    "filename": "fractionehr-assets/digital-intake/4d6fe2cd.png",
    "page": "digital-intake",
    "uid": "4d6fe2cd-201e-45b6-8677-3a2ee72f4174.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/71cf1f87-a2b2-4632-92bd-ab50efa55fa5.png",
    "filename": "fractionehr-assets/clinical-notes/71cf1f87.png",
    "page": "clinical-notes",
    "uid": "71cf1f87-a2b2-4632-92bd-ab50efa55fa5.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/89df424d-bb74-4c31-aaaf-561f5e8f4e10.png",
    "filename": "fractionehr-assets/clinical-notes/89df424d.png",
    "page": "clinical-notes",
    "uid": "89df424d-bb74-4c31-aaaf-561f5e8f4e10.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/c2f955a2-c2e3-482f-bba8-c5fc1efaaee7.png",
    "filename": "fractionehr-assets/clinical-notes/c2f955a2.png",
    "page": "clinical-notes",
    "uid": "c2f955a2-c2e3-482f-bba8-c5fc1efaaee7.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/f60d5fa3-d2e7-4672-a2b6-44da29ffbc42.png",
    "filename": "fractionehr-assets/labs-orders/f60d5fa3.png",
    "page": "labs-orders",
    "uid": "f60d5fa3-d2e7-4672-a2b6-44da29ffbc42.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/4cba3ba5-2135-4e57-838d-481712e64ec6.png",
    "filename": "fractionehr-assets/labs-orders/4cba3ba5.png",
    "page": "labs-orders",
    "uid": "4cba3ba5-2135-4e57-838d-481712e64ec6.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/5c4f3e13-c1a3-4df8-9285-b4800ebb02cb.png",
    "filename": "fractionehr-assets/labs-orders/5c4f3e13.png",
    "page": "labs-orders",
    "uid": "5c4f3e13-c1a3-4df8-9285-b4800ebb02cb.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/0a347b9c-3954-43ef-bf40-022d04622f7b.png",
    "filename": "fractionehr-assets/patient-portal/0a347b9c.png",
    "page": "patient-portal",
    "uid": "0a347b9c-3954-43ef-bf40-022d04622f7b.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/471b9b4a-d940-4c0b-9d97-e7acee6ab8a3.png",
    "filename": "fractionehr-assets/patient-portal/471b9b4a.png",
    "page": "patient-portal",
    "uid": "471b9b4a-d940-4c0b-9d97-e7acee6ab8a3.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/fa942160-361d-4c1c-a98e-e5632d7103cb.png",
    "filename": "fractionehr-assets/patient-portal/fa942160.png",
    "page": "patient-portal",
    "uid": "fa942160-361d-4c1c-a98e-e5632d7103cb.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/93efee3c-c351-41fd-8a57-42ada127cb6b.png",
    "filename": "fractionehr-assets/role-based-access/93efee3c.png",
    "page": "role-based-access",
    "uid": "93efee3c-c351-41fd-8a57-42ada127cb6b.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/2f445559-bef1-4093-9f5d-7e36b9f4bd4f.png",
    "filename": "fractionehr-assets/role-based-access/2f445559.png",
    "page": "role-based-access",
    "uid": "2f445559-bef1-4093-9f5d-7e36b9f4bd4f.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/02f776b4-1b61-4eb0-8b1f-c09e5c3f14d6.png",
    "filename": "fractionehr-assets/role-based-access/02f776b4.png",
    "page": "role-based-access",
    "uid": "02f776b4-1b61-4eb0-8b1f-c09e5c3f14d6.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/c2acf610-d298-4530-8981-3cc02cdf5a9c.png",
    "filename": "fractionehr-assets/appointment-scheduling/c2acf610.png",
    "page": "appointment-scheduling",
    "uid": "c2acf610-d298-4530-8981-3cc02cdf5a9c.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/bdd59a3a-6003-4d19-ba15-f22cfd364906.png",
    "filename": "fractionehr-assets/appointment-scheduling/bdd59a3a.png",
    "page": "appointment-scheduling",
    "uid": "bdd59a3a-6003-4d19-ba15-f22cfd364906.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/84e182a9-f335-4e2d-b914-173e4cb6016e.png",
    "filename": "fractionehr-assets/appointment-scheduling/84e182a9.png",
    "page": "appointment-scheduling",
    "uid": "84e182a9-f335-4e2d-b914-173e4cb6016e.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/828c8993-9f76-48f1-acb6-4824aec26a15.png",
    "filename": "fractionehr-assets/insurance-eligibility/828c8993.png",
    "page": "insurance-eligibility",
    "uid": "828c8993-9f76-48f1-acb6-4824aec26a15.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/1b18f29e-2f1f-4024-a7b0-2153e59b8de2.png",
    "filename": "fractionehr-assets/insurance-eligibility/1b18f29e.png",
    "page": "insurance-eligibility",
    "uid": "1b18f29e-2f1f-4024-a7b0-2153e59b8de2.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/87a645bf-49a9-4de4-b4c4-018d864fb457.png",
    "filename": "fractionehr-assets/insurance-eligibility/87a645bf.png",
    "page": "insurance-eligibility",
    "uid": "87a645bf-49a9-4de4-b4c4-018d864fb457.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/da6ce1a8-7143-4b84-8b16-d6f2485fd75c.png",
    "filename": "fractionehr-assets/eprescribing/da6ce1a8.png",
    "page": "eprescribing",
    "uid": "da6ce1a8-7143-4b84-8b16-d6f2485fd75c.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/cd9f1005-836e-49c6-a28d-2fe778f7f9c6.png",
    "filename": "fractionehr-assets/eprescribing/cd9f1005.png",
    "page": "eprescribing",
    "uid": "cd9f1005-836e-49c6-a28d-2fe778f7f9c6.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/d2f38cf8-7dda-4e28-9f0a-38fc9c469c12.png",
    "filename": "fractionehr-assets/eprescribing/d2f38cf8.png",
    "page": "eprescribing",
    "uid": "d2f38cf8-7dda-4e28-9f0a-38fc9c469c12.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/790de580-cb83-47ba-b66d-5b2b218d546e.png",
    "filename": "fractionehr-assets/billing-claims/790de580.png",
    "page": "billing-claims",
    "uid": "790de580-cb83-47ba-b66d-5b2b218d546e.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/6bc737bd-7a3e-492d-9925-3b2f44aa668d.png",
    "filename": "fractionehr-assets/billing-claims/6bc737bd.png",
    "page": "billing-claims",
    "uid": "6bc737bd-7a3e-492d-9925-3b2f44aa668d.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/cf3b2ddf-cda5-4552-8a29-30be908c367e.png",
    "filename": "fractionehr-assets/billing-claims/cf3b2ddf.png",
    "page": "billing-claims",
    "uid": "cf3b2ddf-cda5-4552-8a29-30be908c367e.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/45d2688d-666d-4a2a-ac30-f8340c57fb69.png",
    "filename": "fractionehr-assets/reports-analytics/45d2688d.png",
    "page": "reports-analytics",
    "uid": "45d2688d-666d-4a2a-ac30-f8340c57fb69.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/ec0bdb46-7dba-484b-a47b-bb3a53767aaa.png",
    "filename": "fractionehr-assets/reports-analytics/ec0bdb46.png",
    "page": "reports-analytics",
    "uid": "ec0bdb46-7dba-484b-a47b-bb3a53767aaa.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/0d1ca630-485d-4698-8ce8-00b994585859.png",
    "filename": "fractionehr-assets/reports-analytics/0d1ca630.png",
    "page": "reports-analytics",
    "uid": "0d1ca630-485d-4698-8ce8-00b994585859.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/c77192be-210b-4b34-95bb-3bbf60fecdc5.png",
    "filename": "fractionehr-assets/data-migration/c77192be.png",
    "page": "data-migration",
    "uid": "c77192be-210b-4b34-95bb-3bbf60fecdc5.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/4d7df420-5f1c-4d95-a2ba-c6ffe5000a89.png",
    "filename": "fractionehr-assets/data-migration/4d7df420.png",
    "page": "data-migration",
    "uid": "4d7df420-5f1c-4d95-a2ba-c6ffe5000a89.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/f332523c-d229-4f45-aa23-38606431d635.png",
    "filename": "fractionehr-assets/data-migration/f332523c.png",
    "page": "data-migration",
    "uid": "f332523c-d229-4f45-aa23-38606431d635.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/2a638885-0a90-4868-8401-d8a94870db81.png",
    "filename": "fractionehr-assets/contact/2a638885.png",
    "page": "contact",
    "uid": "2a638885-0a90-4868-8401-d8a94870db81.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/781a458b-b95a-4004-a231-efd88f5b6826.png",
    "filename": "fractionehr-assets/contact/781a458b.png",
    "page": "contact",
    "uid": "781a458b-b95a-4004-a231-efd88f5b6826.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/0bf3cbeb-efe9-41f2-b34c-4135accb1c57.png",
    "filename": "fractionehr-assets/contact/0bf3cbeb.png",
    "page": "contact",
    "uid": "0bf3cbeb-efe9-41f2-b34c-4135accb1c57.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/89e29f67-8651-4dcb-9667-c05bc4d2885f.png",
    "filename": "fractionehr-assets/contact/89e29f67.png",
    "page": "contact",
    "uid": "89e29f67-8651-4dcb-9667-c05bc4d2885f.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/76de4b94-5804-4083-9a23-0e2a7ed71e7c.png",
    "filename": "fractionehr-assets/contact/76de4b94.png",
    "page": "contact",
    "uid": "76de4b94-5804-4083-9a23-0e2a7ed71e7c.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/827bb1c4-a2a8-4920-b702-8eec55ad3192.png",
    "filename": "fractionehr-assets/contact/827bb1c4.png",
    "page": "contact",
    "uid": "827bb1c4-a2a8-4920-b702-8eec55ad3192.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/cc16c014-d646-402d-8709-152c3445f6a5.png",
    "filename": "fractionehr-assets/contact/cc16c014.png",
    "page": "contact",
    "uid": "cc16c014-d646-402d-8709-152c3445f6a5.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/4e651b17-6d9f-47ff-a7fb-b1ee6418db7a.png",
    "filename": "fractionehr-assets/contact/4e651b17.png",
    "page": "contact",
    "uid": "4e651b17-6d9f-47ff-a7fb-b1ee6418db7a.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/aa66df69-9996-4fe4-b9a6-521b6f9f47b0.png",
    "filename": "fractionehr-assets/contact/aa66df69.png",
    "page": "contact",
    "uid": "aa66df69-9996-4fe4-b9a6-521b6f9f47b0.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/8372f5f6-0ce4-4e45-ac61-d1aa3d54a662.png",
    "filename": "fractionehr-assets/contact/8372f5f6.png",
    "page": "contact",
    "uid": "8372f5f6-0ce4-4e45-ac61-d1aa3d54a662.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/eec54f7b-7bcd-472c-a04a-23dcd348c2d2.png",
    "filename": "fractionehr-assets/contact/eec54f7b.png",
    "page": "contact",
    "uid": "eec54f7b-7bcd-472c-a04a-23dcd348c2d2.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/6587d9ee-c468-4bc6-b461-397eb44a0945.png",
    "filename": "fractionehr-assets/edi-clearing-house/6587d9ee.png",
    "page": "edi-clearing-house",
    "uid": "6587d9ee-c468-4bc6-b461-397eb44a0945.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/e483aa0b-9081-4aff-8716-1659880b4d1f.png",
    "filename": "fractionehr-assets/ehr-247/e483aa0b.png",
    "page": "ehr-247",
    "uid": "e483aa0b-9081-4aff-8716-1659880b4d1f.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/dc8ba7e1-f7cf-4d1d-82f1-5381d1464429.png",
    "filename": "fractionehr-assets/practice-mate/dc8ba7e1.png",
    "page": "practice-mate",
    "uid": "dc8ba7e1-f7cf-4d1d-82f1-5381d1464429.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/130587f3-453f-44c8-b30d-c81c94a906ad.png",
    "filename": "fractionehr-assets/practice-mate/130587f3.png",
    "page": "practice-mate",
    "uid": "130587f3-453f-44c8-b30d-c81c94a906ad.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/3d3f7799-1589-4408-b8ca-fc060d1db806.png",
    "filename": "fractionehr-assets/practice-mate/3d3f7799.png",
    "page": "practice-mate",
    "uid": "3d3f7799-1589-4408-b8ca-fc060d1db806.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/1259dca2-b75e-4670-9021-f80cc18af641.png",
    "filename": "fractionehr-assets/practice-mate/1259dca2.png",
    "page": "practice-mate",
    "uid": "1259dca2-b75e-4670-9021-f80cc18af641.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/ace2f624-c4fd-4bd8-950f-9766452023d7.png",
    "filename": "fractionehr-assets/company/ace2f624.png",
    "page": "company",
    "uid": "ace2f624-c4fd-4bd8-950f-9766452023d7.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/764e2086-83f0-4986-972d-e0bc3eda3051.png",
    "filename": "fractionehr-assets/company/764e2086.png",
    "page": "company",
    "uid": "764e2086-83f0-4986-972d-e0bc3eda3051.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/1ac43882-ff7b-4a23-8353-5a5d08e71ba3.png",
    "filename": "fractionehr-assets/company/1ac43882.png",
    "page": "company",
    "uid": "1ac43882-ff7b-4a23-8353-5a5d08e71ba3.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/4d2b1f50-3816-4e3e-bea8-fcc4091cd959.png",
    "filename": "fractionehr-assets/company/4d2b1f50.png",
    "page": "company",
    "uid": "4d2b1f50-3816-4e3e-bea8-fcc4091cd959.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/911443d5-a6a4-4705-a0dd-09c39868e3d0.png",
    "filename": "fractionehr-assets/company/911443d5.png",
    "page": "company",
    "uid": "911443d5-a6a4-4705-a0dd-09c39868e3d0.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/cee2e3d2-981c-4e1c-aa0b-183f80b9e0d0.png",
    "filename": "fractionehr-assets/company/cee2e3d2.png",
    "page": "company",
    "uid": "cee2e3d2-981c-4e1c-aa0b-183f80b9e0d0.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/5b8d7e56-dc2b-424e-9d78-1f9da6c2e49f.png",
    "filename": "fractionehr-assets/company/5b8d7e56.png",
    "page": "company",
    "uid": "5b8d7e56-dc2b-424e-9d78-1f9da6c2e49f.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/35afc3da-a6f4-4dd4-8b3e-8292165a9639.png",
    "filename": "fractionehr-assets/company/35afc3da.png",
    "page": "company",
    "uid": "35afc3da-a6f4-4dd4-8b3e-8292165a9639.png"
  },
  {
    "url": "https://www.figma.com/api/mcp/asset/df642f0c-ef2d-46d1-a8e0-f9b75a4c7ecd.png",
    "filename": "fractionehr-assets/company/df642f0c.png",
    "page": "company",
    "uid": "df642f0c-ef2d-46d1-a8e0-f9b75a4c7ecd.png"
  }
]

print(f"Downloading {len(images)} images...")
ok, fail = [], []

for i, img in enumerate(images, 1):
    try:
        os.makedirs(os.path.dirname(img["filename"]), exist_ok=True)
        urllib.request.urlretrieve(img["url"], img["filename"])
        ok.append(img["filename"])
        print(f"[{i:02d}/{len(images)}] OK  {img['filename']}")
    except Exception as e:
        fail.append(img["filename"])
        print(f"[{i:02d}/{len(images)}] ERR {img['filename']} — {e}")
    time.sleep(0.3)

print(f"\n✓ Downloaded: {len(ok)}")
if fail:
    print(f"✗ Failed:     {len(fail)}")
    for f in fail: print(f"   {f}")
    print("\nTell Claude which ones failed — they will be refreshed from Figma.")
else:
    print("All images downloaded! Upload the fractionehr-assets/ folder to GitHub.")
