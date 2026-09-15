<div align="center">

# Flask Service Backend
### Multi-role REST-style backend prototype

![Python](https://img.shields.io/badge/Python-Flask-blue)
![API](https://img.shields.io/badge/Type-Web%20API-green)

</div>

## Overview

This repository contains an earlier **Flask-based backend service** with APIs for users, riders, sellers, and administrators. The project covers account management, ordering, search, uploads, and role-specific service flows.

## API Groups

### User

- `/user/login` — user login
- `/user/register` — registration with email verification
- `/user/cancellation` — account cancellation
- `/user/changePassword` — password update
- `/user/changeName` — profile-name update
- `/user/follow` — follow operation
- `/user/order` — place an order
- `/user/serchBySeller` — search by seller
- `/user/serchByGoods` — search by goods
- `/user/serchByClassfication` — search by category
- `/user/upload_user` — upload user avatar

### Rider

- `/rider/login` — rider login
- `/rider/task` — accept delivery task
- `/rider/income` — query rider income

### Seller

- `/seller/like` — like interaction
- `/seller/collection` — collection/favorite interaction
- `/seller/forward` — forwarding interaction
- `/seller/comment` — comments
- `/seller/upload_seller` — upload product/media information

### Admin

- `/admin/...` — administrative CRUD operations

## Project Scope

The project was built as a practical backend-development exercise. It demonstrates:

- multi-role API design,
- account and authentication workflows,
- email-verification-related flows,
- order/task handling,
- search endpoints,
- file/media upload handling,
- administrative CRUD operations.

## Notes

The endpoint names above preserve the original implementation, including legacy spelling such as `serchBy...`. This repository is kept as part of my earlier software-development portfolio and may require environment/database configuration before it can be run on a new machine.

## Author

**Bo Liu**  
Contact: `liubo317@hnu.edu.cn`
