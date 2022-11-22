
create table USUARIO
(
   E_MAIL               varchar(60) not null,
   NOMBRE       		varchar(60) not null,
   CONTRASENA           varchar(60) not null,
   DIRECCION            varchar(60) not null,
   TARJETA              varchar(60) not null,
   PUNTOS			bigint,
   primary key (E_MAIL)
);


create table ORDEN
(
   E_MAIL_CLIENTE           varchar(60) not null,
   ID_PRODUCTO    	    bigint not null,
   CODIGO_ORDEN             bigint not null,
   ESTADO_ENTREGA           varchar(30) not null,
   CANTIDAD_PRODUCTO        bigint not null,
   HORARIO_ENTREGA	    date not null,
   PAPEL_REGALO		    varchar(60),
   CINTA			    varchar(60),
   MENSAJE			    varchar(60),

   primary key (E_MAIL_CLIENTE,ID_PRODUCTO,CODIGO_ORDEN)
);


create table PRODUCTO
(
   ID_PRODUCTO       bigint not null,
   NOMBRE            varchar(50) not null,
   IMAGEN            varchar(50) not null,
   DESCRIPCION  	   varchar(200) not null,
   PRECIO            bigint not null,
   NIT_EMPRESA       bigint not null,
   INVENTARIO        bigint not null,
   DESCUENTO	   bigint,
   primary key (ID_PRODUCTO)
);


create table EMPRESA
(
   NIT       		bigint not null,
   NOMBRE         	varchar(50) not null,
   NUMERO_CONTACTO      bigint not null,
   PERFIL_REDES  		varchar(50) not null,
   DIRECCION            varchar(200) not null, 
   primary key (NIT)
);

create table ADMINISTRADOR
(
   E_MAIL               varchar(60) not null,
   NOMBRE       		varchar(60) not null,
   CONTRASENA           varchar(60) not null,
   primary key (E_MAIL)
);


alter table PRODUCTO add constraint FK_PR foreign key (NIT_EMPRESA)
      references EMPRESA (NIT) on delete restrict on update restrict;

alter table ORDEN add constraint FK_ORPR foreign key (ID_PRODUCTO)
      references PRODUCTO (ID_PRODUCTO) on delete restrict on update restrict;

alter table ORDEN add constraint FK_ORUS foreign key (E_MAIL_CLIENTE)
      references USUARIO (E_MAIL) on delete restrict on update restrict;
